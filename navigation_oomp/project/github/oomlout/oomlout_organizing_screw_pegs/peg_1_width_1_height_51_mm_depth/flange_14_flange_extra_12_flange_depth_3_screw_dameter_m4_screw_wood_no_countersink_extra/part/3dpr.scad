$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -51.0000000000]) {
			cylinder(h = 51, r = 7.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 13.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -51]) {
			cylinder(h = 51, r = 2.2500000000);
		}
	}
}