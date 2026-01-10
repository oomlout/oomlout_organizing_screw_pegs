$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -90.0000000000]) {
			cylinder(h = 90, r = 7.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 10.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -90]) {
			cylinder(h = 90, r = 2.7500000000);
		}
	}
}