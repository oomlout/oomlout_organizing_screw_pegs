$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -140.0000000000]) {
			cylinder(h = 140, r = 7.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 13.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -140]) {
			cylinder(h = 140, r = 3.2500000000);
		}
	}
}