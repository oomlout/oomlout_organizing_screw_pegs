$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -51.0000000000]) {
			cylinder(h = 51, r = 10.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 19.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -51]) {
			cylinder(h = 51, r = 1.8000000000);
		}
	}
}