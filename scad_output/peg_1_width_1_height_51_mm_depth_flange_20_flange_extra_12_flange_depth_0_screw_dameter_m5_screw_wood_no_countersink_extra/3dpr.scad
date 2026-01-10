$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -51.0000000000]) {
			cylinder(h = 51, r = 10.0000000000);
		}
		cylinder(h = 0, r = 16.0000000000);
	}
	union() {
		#translate(v = [0, 0, -51]) {
			cylinder(h = 51, r = 2.7500000000);
		}
	}
}