$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -45.0000000000]) {
			cylinder(h = 45, r = 10.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 20.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -45]) {
			cylinder(h = 45, r = 2.2500000000);
		}
	}
}