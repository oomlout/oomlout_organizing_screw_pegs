"""Flask web server that renders pages from the web_pages_oomp directory."""

import html
import json
import os
from datetime import datetime
from importlib import import_module, reload
from pathlib import Path, PureWindowsPath
from typing import Any, Dict, List, Optional, Set, Tuple

from flask import Flask, abort, render_template, request, send_from_directory, url_for
from jinja2 import TemplateNotFound

try:
    from pygments import highlight
    from pygments.formatters import HtmlFormatter
    from pygments.lexers import YamlLexer
except ImportError:  # pragma: no cover - optional dependency
    highlight = None
    HtmlFormatter = None
    YamlLexer = None

try:
    import yaml
except ImportError:  # pragma: no cover - handled at runtime
    yaml = None
BIP39_WORDLIST_SOURCE: Optional[Path] = None
BASE_DIR = Path(__file__).parent
BIP39_WORDLIST_PATH = BASE_DIR / "web_pages_oomp" / "static" / "data" / "bip39_wordlist.txt"
PARTS_DIR = BASE_DIR / "parts"
PART_SOURCE_SPECS: List[Tuple[str, Any]] = []
PART_SOURCE_SPECS.append(("base_parts", PARTS_DIR))
# Z:\oomlout_oomp_version_1_messy oomp_main
#PART_SOURCE_SPECS.append(("oomp_main", r"Z:\oomlout_oomp_version_1_messy\parts"))


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"}
OOMP_TAXONOMY_FIELDS: List[str] = [
    "classification",
    "type",
    "size",
    "color",
    "description_main",
    "description_extra",
    "manufacturer",
    "part_number",
]
TAXONOMY_EMPTY_LABEL = "unspecified"
if HtmlFormatter is not None:
    PYGMENTS_FORMATTER = HtmlFormatter(style="friendly", cssclass="codehilite", nowrap=False)
    PYGMENTS_CSS = PYGMENTS_FORMATTER.get_style_defs(".codehilite")
else:
    PYGMENTS_FORMATTER = None
    PYGMENTS_CSS = ""


def _timestamp() -> str:
    """Return a UTC timestamp string for logging."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def _json_default(value: Any) -> str:
    """Serialize unsupported JSON types as strings for caching."""
    return str(value)


def _candidate_bip39_wordlists() -> List[Path]:
    """Return candidate paths to search for the BIP-39 word list."""
    candidates: List[Path] = []

    env_path = os.getenv("BIP39_WORDLIST")
    if env_path:
        candidates.append(Path(env_path))

    candidates.append(BIP39_WORDLIST_PATH)

    utility_repo = BASE_DIR.parent / "oomlout_oomp_utility_oomlout_short_code" / "source" / "bip_39_wordlist.txt"
    candidates.append(utility_repo)

    # Remove duplicates while preserving order.
    seen: Set[Path] = set()
    unique: List[Path] = []
    for candidate in candidates:
        try:
            resolved = candidate.expanduser()
        except Exception:
            continue
        if resolved not in seen:
            unique.append(resolved)
            seen.add(resolved)
    return unique


def _load_bip39_wordlist() -> List[str]:
    """Load the BIP-39 word list from disk."""
    global BIP39_WORDLIST_SOURCE

    for candidate in _candidate_bip39_wordlists():
        if candidate.exists():
            try:
                with candidate.open("r", encoding="utf-8") as handle:
                    words = [line.strip() for line in handle if line.strip()]
                    if words:
                        BIP39_WORDLIST_SOURCE = candidate
                        return words
            except OSError:
                continue

    BIP39_WORDLIST_SOURCE = None
    return []


BIP39_WORDLIST = _load_bip39_wordlist()


def _md5_to_bip39_words(md5_hex: str) -> List[str]:
    """Convert an MD5 hex string into a list of BIP-39 words."""
    if not md5_hex or not BIP39_WORDLIST:
        return []
    try:
        value = int(md5_hex, 16)
    except ValueError:
        return []

    word_count = len(BIP39_WORDLIST)
    if word_count == 0:
        return []

    if value == 0:
        return [BIP39_WORDLIST[0]]

    indices: List[int] = []
    # Limit to a reasonable number of words to avoid runaway loops.
    while value > 0 and len(indices) < 24:
        indices.append(value % word_count)
        value //= word_count

    return [BIP39_WORDLIST[index] for index in indices]


def _expand_candidates(raw_path: str) -> List[Path]:
    """Build a list of candidate filesystem paths for the given raw string."""
    candidates: List[Path] = []
    if not raw_path:
        return candidates

    normalized = raw_path.replace("\\", "/")
    for path_str in {raw_path, normalized}:
        try:
            candidates.append(Path(path_str))
        except TypeError:
            continue

    try:
        win_path = PureWindowsPath(raw_path)
        if win_path.drive:
            drive_letter = win_path.drive.rstrip(":").lower()
            wsl_candidate = Path("/mnt") / drive_letter
            for part in win_path.parts[1:]:
                wsl_candidate /= part
            candidates.append(wsl_candidate)
    except Exception:
        pass

    unique_candidates: List[Path] = []
    for candidate in candidates:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
    return unique_candidates


def _resolve_path(raw_paths: List[str]) -> Path:
    """Return the first existing path from the provided raw path candidates."""
    candidates: List[Path] = []
    for raw_path in raw_paths:
        candidates.extend(_expand_candidates(raw_path))

    for candidate in candidates:
        if candidate.exists():
            return candidate

    if candidates:
        return candidates[0]
    return Path(raw_paths[0]) if raw_paths else Path.cwd()


def _load_yaml_group(source_dir: Path, group_name: str) -> Dict[str, Any]:
    """Load all YAML files under a directory with simple console progress."""
    if yaml is None:
        print(f"[setup] {group_name}: PyYAML is not available; skipping load.", flush=True)
        return {}

    if not source_dir.exists():
        print(f"[setup] {group_name}: directory {source_dir} not found; skipping.", flush=True)
        return {}

    yaml_files = sorted(source_dir.rglob("*.yaml"))
    bundle_path = source_dir / f".{group_name}_bundle.json"

    current_meta: Dict[str, Dict[str, float]] = {}
    for file_path in yaml_files:
        try:
            stat = file_path.stat()
        except OSError:
            continue
        relative_name = file_path.relative_to(source_dir).as_posix()
        current_meta[relative_name] = {"mtime": stat.st_mtime, "size": float(stat.st_size)}

    cached_files: Dict[str, Any] = {}
    cached_meta: Dict[str, Dict[str, float]] = {}
    if bundle_path.exists():
        try:
            with bundle_path.open("r", encoding="utf-8") as handle:
                cache_payload = json.load(handle)
            raw_files = cache_payload.get("files") or {}
            raw_meta = cache_payload.get("meta") or {}
            cached_files = {key.replace("\\", "/"): value for key, value in raw_files.items()}
            cached_meta = {
                key.replace("\\", "/"): {
                    "mtime": float(meta.get("mtime", 0.0)),
                    "size": float(meta.get("size", 0.0)),
                }
                for key, meta in raw_meta.items()
                if isinstance(meta, dict)
            }
            print(
                f"[setup] {group_name}: cache {bundle_path.name} loaded "
                f"({len(cached_files)} cached records).",
                flush=True,
            )
        except Exception as exc:  # pragma: no cover - defensive logging
            print(
                f"[setup] {group_name}: failed to read cache {bundle_path.name} -> {exc}; rebuilding.",
                flush=True,
            )
            cached_files = {}
            cached_meta = {}

    reload_paths = [
        rel_path
        for rel_path, meta in current_meta.items()
        if rel_path not in cached_meta
        or cached_meta[rel_path].get("mtime", 0.0) < meta["mtime"]
        or cached_meta[rel_path].get("size", -1.0) != meta["size"]
    ]
    removed_paths = [rel_path for rel_path in cached_files if rel_path not in current_meta]

    start_time = _timestamp()
    print(
        f"[setup] {group_name}: starting load at {start_time} from {source_dir} "
        f"({len(reload_paths)} changes; {len(yaml_files)} total files)",
        flush=True,
    )

    loaded: Dict[str, Any] = dict(cached_files)
    errors = 0
    printed_dots = False

    for index, relative_name in enumerate(reload_paths, start=1):
        file_path = source_dir / relative_name
        try:
            with file_path.open("r", encoding="utf-8") as handle:
                loaded[relative_name] = yaml.safe_load(handle)
        except Exception as exc:  # pragma: no cover - defensive logging
            print(f"\n[setup] {group_name}: failed to load {file_path} -> {exc}", flush=True)
            errors += 1
            continue

        if index % 100 == 0:
            print(".", end="", flush=True)
            printed_dots = True

    for relative_name in removed_paths:
        loaded.pop(relative_name, None)

    if printed_dots:
        print("", flush=True)

    end_time = _timestamp()
    details = (
        f"{len(loaded)} files cached; {len(reload_paths)} reloaded"
        + (f"; {len(removed_paths)} removed" if removed_paths else "")
    )
    if errors:
        details += f"; {errors} errors"

    print(
        f"[setup] {group_name}: finished load at {end_time}; {details}.",
        flush=True,
    )

    cache_payload = {
        "generated": end_time,
        "file_count": len(loaded),
        "meta": current_meta,
        "files": loaded,
    }
    try:
        with bundle_path.open("w", encoding="utf-8") as handle:
            json.dump(cache_payload, handle, default=_json_default)
        current_timestamp = datetime.utcnow().timestamp()
        os.utime(bundle_path, (current_timestamp, current_timestamp))
        print(
            f"[setup] {group_name}: cached bundle written to {bundle_path.name}.",
            flush=True,
        )
    except Exception as exc:  # pragma: no cover - defensive logging
        print(f"[setup] {group_name}: failed to write cache -> {exc}", flush=True)

    return loaded


PART_GROUPS: Dict[str, Dict[str, Any]] = {}
PART_SOURCE_DIRS: Dict[str, Path] = {}
BASE_PARTS: Dict[str, Any] = {}
BASE_PARTS_DIR_RESOLVED: Path = PARTS_DIR
PART_INDEX: Dict[str, Dict[str, Any]] = {}
TAXONOMY_TREES: Dict[str, Any] = {}

def _derive_top_category(relative_path: str) -> str:
    """Return the top-level folder for the relative path, if available."""
    clean_path = relative_path.replace("\\", "/")
    return clean_path.split("/", 1)[0] if "/" in clean_path else clean_path


def _build_part_index() -> Dict[str, Dict[str, Any]]:
    """Create a dictionary of part metadata keyed by group and part id."""
    index: Dict[str, Dict[str, Any]] = {}
    for group_name, parts in PART_GROUPS.items():
        group_index: Dict[str, Any] = {}
        for rel_path, payload in parts.items():
            if not isinstance(payload, dict):
                continue
            normalized_path = rel_path.replace("\\", "/")
            part_id = payload.get("id") or normalized_path.rsplit("/", 1)[0]
            relative_dir = Path(normalized_path).parent
            top_category = payload.get("classification") or _derive_top_category(rel_path)
            md5_hex = str(payload.get("md5", "")).strip().lower()
            words = _md5_to_bip39_words(md5_hex)[:3]
            search_terms = [top_category, part_id, *words]
            search_blob = " ".join(term for term in search_terms if term).lower()
            group_index[part_id] = {
                "id": part_id,
                "top_category": top_category,
                "rel_path": rel_path,
                "data": payload,
                "relative_dir": relative_dir,
                "search_blob": search_blob,
                "words": words,
            }
        index[group_name] = group_index
    return index


PART_INDEX = _build_part_index()


def _taxonomy_value(data: Dict[str, Any], field: str) -> str:
    """Extract a taxonomy field value with fallback handling."""
    value = data.get(field)
    if isinstance(value, list):
        value = ", ".join(str(item) for item in value if item not in (None, ""))
    elif isinstance(value, dict):
        value = ", ".join(f"{key}: {val}" for key, val in value.items())
    if value is None:
        return TAXONOMY_EMPTY_LABEL
    text = str(value).strip()
    return text or TAXONOMY_EMPTY_LABEL


def _build_taxonomy_tree(parts: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Construct a nested taxonomy tree for a group of parts."""
    tree: Dict[str, Any] = {}
    field_count = len(OOMP_TAXONOMY_FIELDS)

    for part_id, info in parts.items():
        payload = info.get("data") or {}
        node = tree
        parent_entry: Optional[Dict[str, Any]] = None
        inserted = False

        for idx, field in enumerate(OOMP_TAXONOMY_FIELDS):
            label = _taxonomy_value(payload, field)

            if label == TAXONOMY_EMPTY_LABEL:
                continue

            entry = node.setdefault(
                label,
                {
                    "count": 0,
                    "children": {},
                    "parts": [],
                },
            )
            entry["count"] = entry.get("count", 0) + 1
            if idx == field_count - 1:
                entry.setdefault("parts", []).append(part_id)

            parent_entry = entry
            node = entry.setdefault("children", {})
            inserted = True
        else:
            # No taxonomy fields triggered a break but parent_entry may be None (no fields configured)
            if not inserted:
                tree.setdefault("_parts", []).append(part_id)
            elif parent_entry is not None and part_id not in parent_entry.setdefault("parts", []):
                parent_entry.setdefault("parts", []).append(part_id)

    return tree


def _format_taxonomy_branch(tree: Dict[str, Dict[str, Any]], group: str, level: int = 0) -> List[Dict[str, Any]]:
    """Convert a taxonomy tree into a template-friendly structure."""
    formatted: List[Dict[str, Any]] = []
    for label, entry in sorted(
        ((key, value) for key, value in tree.items() if key != "_parts"),
        key=lambda item: item[0],
    ):
        children_tree = entry.get("children", {})
        parts_list = sorted(entry.get("parts", []))
        count = entry.get("count", 0)
        formatted.append(
            {
                "label": label,
                "count": count,
                "level": level,
                "parts": [
                    {
                        "id": part_id,
                        "detail_url": url_for("part_detail", group=group, part_id=part_id),
                    }
                    for part_id in parts_list
                ],
                "children": _format_taxonomy_branch(children_tree, group, level + 1)
                if children_tree
                else [],
            }
        )
    return formatted


def _build_navigation_taxonomy() -> Dict[str, Any]:
    """Prepare navigation taxonomy data for templates."""
    taxonomy: Dict[str, Any] = {}
    for group_name, parts in PART_INDEX.items():
        taxonomy[group_name] = _build_taxonomy_tree(parts)
    return taxonomy


def _reload_data() -> Dict[str, Any]:
    """Reload part datasets and derived indexes from disk."""
    global BIP39_WORDLIST
    global PART_GROUPS
    global PART_SOURCE_DIRS
    global BASE_PARTS
    global BASE_PARTS_DIR_RESOLVED
    global PART_INDEX
    global TAXONOMY_TREES

    BIP39_WORDLIST = _load_bip39_wordlist()

    new_part_groups: Dict[str, Dict[str, Any]] = {}
    new_part_source_dirs: Dict[str, Path] = {}

    for short_name, raw_directory in PART_SOURCE_SPECS:
        if not raw_directory:
            continue

        if isinstance(raw_directory, (list, tuple)):
            raw_paths = [str(path) for path in raw_directory if path]
        else:
            raw_paths = [str(raw_directory)]

        resolved_dir = _resolve_path(raw_paths)
        new_part_source_dirs[short_name] = resolved_dir
        new_part_groups[short_name] = _load_yaml_group(resolved_dir, short_name)

    PART_GROUPS = new_part_groups
    PART_SOURCE_DIRS = new_part_source_dirs

    BASE_PARTS = PART_GROUPS.get("base_parts", {})
    BASE_PARTS_DIR_RESOLVED = PART_SOURCE_DIRS.get("base_parts", PARTS_DIR)

    PART_INDEX = _build_part_index()
    TAXONOMY_TREES = _build_navigation_taxonomy()

    total_parts = sum(len(group) for group in PART_GROUPS.values())
    indexed_parts = sum(len(group) for group in PART_INDEX.values())

    return {
        "timestamp": _timestamp(),
        "group_count": len(PART_GROUPS),
        "source_paths": {name: str(path) for name, path in PART_SOURCE_DIRS.items()},
        "raw_part_count": total_parts,
        "indexed_part_count": indexed_parts,
        "bip39_word_count": len(BIP39_WORDLIST),
        "bip39_wordlist_path": str(BIP39_WORDLIST_SOURCE) if BIP39_WORDLIST_SOURCE else None,
    }


_LAST_RELOAD_SUMMARY: Dict[str, Any] = {}


TEMPLATE_DIR = BASE_DIR / "web_pages_oomp"
STATIC_DIR = TEMPLATE_DIR / "static"
SITE_TITLE = "Flask Oomp Navigator"
app = Flask(
    __name__,
    template_folder=str(TEMPLATE_DIR),
    static_folder=str(STATIC_DIR),
)
app.config["SITE_TITLE"] = SITE_TITLE
app.config["pygments_css"] = PYGMENTS_CSS


def _update_app_config() -> None:
    """Synchronize Flask config values with the latest datasets."""
    app.config["parts"] = BASE_PARTS
    app.config["part_groups"] = PART_GROUPS
    app.config["parts_sources"] = {name: str(path) for name, path in PART_SOURCE_DIRS.items()}
    app.config["taxonomy"] = {
        name: PART_GROUPS.get(name, {}) for name in PART_GROUPS
    }
    app.config["part_index"] = PART_INDEX
    app.config["taxonomy_fields"] = OOMP_TAXONOMY_FIELDS
    app.config["taxonomy_trees"] = TAXONOMY_TREES
    app.config["bip39_words"] = BIP39_WORDLIST
    app.config["total_part_count"] = sum(len(group) for group in PART_INDEX.values())
    app.config["last_reload"] = _LAST_RELOAD_SUMMARY
    app.config["bip39_wordlist_path"] = str(BIP39_WORDLIST_SOURCE) if BIP39_WORDLIST_SOURCE else None


_LAST_RELOAD_SUMMARY = _reload_data()
_update_app_config()


def _load_page_hooks():
    """Load (and hot-reload) the optional page hook module."""
    module_name = "web_pages_oomp.page_hooks"
    try:
        if module_name in globals().get("_hook_cache", {}):
            module = reload(globals()["_hook_cache"][module_name])
        else:
            module = import_module(module_name)
        globals().setdefault("_hook_cache", {})[module_name] = module
        return module
    except ModuleNotFoundError:
        return None


def _derive_page_title(template_name: str) -> str:
    """Return a fallback page title based on the template name."""
    base_name = template_name.rsplit(".", 1)[0]
    return base_name.replace("_", " ").title()


def render_page(template_name: str, **context: Any):
    """Render a template and run optional hooks around the render."""
    hooks = _load_page_hooks()
    context_data: Dict[str, Any] = {
        "site_title": app.config.get("SITE_TITLE", SITE_TITLE),
        "request_method": request.method,
        "pygments_css": app.config.get("pygments_css"),
    }
    context_data.update(context)
    context_data.setdefault("page_title", _derive_page_title(template_name))

    hook_meta: Dict[str, Any] = {"template": template_name}
    if hooks and hasattr(hooks, "before_render"):
        extra = hooks.before_render(template_name, context_data)
        if isinstance(extra, dict):
            context_data.update(extra)
        hook_meta["hook_module"] = getattr(hooks, "__name__", "web_pages_oomp.page_hooks")
    else:
        hook_meta["hook_module"] = None

    context_keys = sorted(context_data.keys())
    context_data.setdefault("debug_info", {}).update({**hook_meta, "context_keys": context_keys})
    app.logger.debug("Rendering %s with context keys: %s", template_name, context_keys)

    try:
        return render_template(template_name, **context_data)
    except TemplateNotFound:
        abort(404)


def _collect_filter_entries() -> List[Dict[str, Any]]:
    """Flatten the part index into a list for the filter view."""
    entries: List[Dict[str, Any]] = []
    for group_name, group_index in PART_INDEX.items():
        for part_id, info in group_index.items():
            words = info.get("words") or []
            words_lower = [word.lower() for word in words]
            search_parts = [
                info.get("search_blob", ""),
                group_name.lower(),
                " ".join(words_lower),
            ]
            search_blob = " ".join(part for part in search_parts if part).strip()
            entries.append(
                {
                    "group": group_name,
                    "id": part_id,
                    "top_category": info["top_category"],
                    "search_blob": search_blob,
                    "words": words,
                }
            )
    entries.sort(key=lambda item: (item["group"], item["id"]))
    return entries


def _collect_bip39_entries() -> List[Dict[str, Any]]:
    """Return part entries that have at least three BIP-39 words."""
    entries: List[Dict[str, Any]] = []
    for group_name, group_index in PART_INDEX.items():
        for part_id, info in group_index.items():
            words = info.get("words") or []
            if len(words) < 3:
                continue
            entries.append(
                {
                    "group": group_name,
                    "id": part_id,
                    "top_category": info.get("top_category"),
                    "words": words,
                }
            )
    entries.sort(key=lambda item: (item["words"], item["group"], item["id"]))
    return entries


def _collect_part_images(group: str, part_info: Dict[str, Any]) -> List[Dict[str, str]]:
    """Gather image metadata for a part directory."""
    base_dir = PART_SOURCE_DIRS.get(group)
    if not base_dir:
        return []

    relative_dir: Path = part_info.get("relative_dir", Path("."))
    part_dir = (base_dir / relative_dir).resolve()
    if not part_dir.exists() or not part_dir.is_dir():
        return []

    images: List[Dict[str, str]] = []
    for image_path in sorted(part_dir.iterdir()):
        if not image_path.is_file():
            continue
        if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        rel_asset = image_path.relative_to(base_dir).as_posix()
        images.append(
            {
                "filename": image_path.name,
                "url": url_for("part_media", group=group, asset_path=rel_asset),
            }
        )
    return images


@app.route("/reload", methods=["GET", "POST"])
def reload_data_view():
    """Reload cached data from disk and display the current snapshot."""
    global _LAST_RELOAD_SUMMARY

    should_reload = (
        request.method == "POST"
        or request.args.get("refresh") == "1"
        or not _LAST_RELOAD_SUMMARY
    )

    if should_reload:
        _LAST_RELOAD_SUMMARY = _reload_data()
        _update_app_config()

    return render_page(
        "reload.html",
        page_title="Reload Data",
        reload_summary=_LAST_RELOAD_SUMMARY,
        page_meta={"highlight": "reload"},
    )


@app.route("/oomp_navigation")
def oomp_navigation():
    """Explore the configured taxonomy levels for all part groups."""
    navigation_tree: Dict[str, Dict[str, Any]] = {}
    for group, tree in sorted(TAXONOMY_TREES.items(), key=lambda item: item[0]):
        nodes = _format_taxonomy_branch(tree, group)
        root_parts = [
            {
                "id": part_id,
                "detail_url": url_for("part_detail", group=group, part_id=part_id),
            }
            for part_id in sorted(tree.get("_parts", []))
        ]
        navigation_tree[group] = {
            "nodes": nodes,
            "root_parts": root_parts,
        }

    group_totals = {group: len(PART_INDEX.get(group, {})) for group in navigation_tree}
    total_parts = sum(group_totals.values())

    return render_page(
        "oomp_navigation.html",
        page_title="OOMP Navigation",
        taxonomy_fields=OOMP_TAXONOMY_FIELDS,
        navigation_tree=navigation_tree,
        group_totals=group_totals,
        total_parts=total_parts,
        page_meta={"highlight": "oomp_navigation"},
    )


@app.route("/bip39_navigation")
def bip39_navigation():
    """Navigate parts by their third BIP-39 word."""
    entries = _collect_bip39_entries()
    enriched = [
        {
            **entry,
            "detail_url": url_for("part_detail", group=entry["group"], part_id=entry["id"]),
        }
        for entry in entries
    ]

    return render_page(
        "bip39_navigation.html",
        page_title="BIP-39 Navigation",
        bip39_entries=enriched,
        bip39_words=BIP39_WORDLIST,
        total_parts=len(enriched),
        page_meta={"highlight": "bip39_navigation"},
    )


@app.route("/filter")
def filter_parts():
    """Interactive filter page for browsing parts."""
    entries = _collect_filter_entries()
    enriched = [
        {
            **entry,
            "detail_url": url_for("part_detail", group=entry["group"], part_id=entry["id"]),
        }
        for entry in entries
    ]
    return render_page(
        "filter.html",
        page_title="Part Filter",
        part_entries=enriched,
        total_parts=len(entries),
        page_meta={"highlight": "filter"},
    )


@app.route("/parts/<group>/<path:part_id>")
def part_detail(group: str, part_id: str):
    """Display detail for a single part."""
    group_index = PART_INDEX.get(group)
    if not group_index:
        abort(404)

    part_info = group_index.get(part_id)
    if not part_info:
        abort(404)

    part_images = _collect_part_images(group, part_info)
    source_dir = PART_SOURCE_DIRS.get(group)
    relative_dir: Path = part_info.get("relative_dir", Path("."))
    relative_dir_str = relative_dir.as_posix() if str(relative_dir) != "." else "."

    yaml_relative_path = part_info.get("rel_path")
    absolute_yaml_path = None
    if source_dir:
        absolute_yaml_path = (source_dir / Path(yaml_relative_path)).resolve()

    part_context = {
        "group": group,
        "id": part_info.get("id"),
        "top_category": part_info.get("top_category"),
        "data": part_info.get("data"),
        "relative_dir": relative_dir_str,
        "relative_yaml_path": yaml_relative_path,
        "source_root": str(source_dir) if source_dir else None,
        "absolute_yaml_path": str(absolute_yaml_path) if absolute_yaml_path else None,
        "search_blob": part_info.get("search_blob"),
    }

    raw_yaml = ""
    if yaml is not None:
        raw_yaml = yaml.safe_dump(part_context["data"], sort_keys=True, allow_unicode=True)
    else:
        raw_yaml = json.dumps(part_context["data"], indent=2, default=_json_default)

    if raw_yaml and highlight is not None and PYGMENTS_FORMATTER is not None and YamlLexer is not None:
        highlighted_yaml = highlight(raw_yaml, YamlLexer(), PYGMENTS_FORMATTER)
    elif raw_yaml:
        highlighted_yaml = f"<pre>{html.escape(raw_yaml)}</pre>"
    else:
        highlighted_yaml = ""

    return render_page(
        "part_detail.html",
        page_title=f"Part: {part_context['id']}",
        part=part_context,
        part_images=part_images,
        part_yaml_html=highlighted_yaml,
    )


@app.route("/parts_media/<group>/<path:asset_path>")
def part_media(group: str, asset_path: str):
    """Serve supporting part assets such as images."""
    base_dir = PART_SOURCE_DIRS.get(group)
    if not base_dir:
        abort(404)

    resolved_base = base_dir.resolve()
    target_path = (resolved_base / asset_path).resolve()
    if not str(target_path).startswith(str(resolved_base)):
        abort(404)
    if not target_path.exists():
        abort(404)

    return send_from_directory(resolved_base, asset_path)


@app.route("/")
def index():
    """Serve the index page."""
    return render_page("index.html", page_title="Flask Index")


@app.route("/example_form", methods=["GET", "POST"])
def example_form():
    """Minimal example form handler."""
    return render_page("example_form.html", page_title="Example Form")


@app.route("/<path:page_name>")
def serve_page(page_name: str):
    """Serve any template from the web_pages_oomp directory."""
    template_name = page_name if page_name.endswith(".html") else f"{page_name}.html"
    return render_page(template_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    
