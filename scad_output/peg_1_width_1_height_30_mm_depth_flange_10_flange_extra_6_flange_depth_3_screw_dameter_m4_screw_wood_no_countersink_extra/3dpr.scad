$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -30.0000000000]) {
			cylinder(h = 30, r = 5.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 8.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -30]) {
			cylinder(h = 30, r = 2.2500000000);
		}
	}
}