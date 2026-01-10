$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -39.0000000000]) {
			cylinder(h = 39, r = 7.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 13.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -39]) {
			cylinder(h = 39, r = 2.2500000000);
		}
	}
}