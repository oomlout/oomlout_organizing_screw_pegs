$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -80.0000000000]) {
			cylinder(h = 80, r = 7.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 16.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -80]) {
			cylinder(h = 80, r = 2.2500000000);
		}
	}
}