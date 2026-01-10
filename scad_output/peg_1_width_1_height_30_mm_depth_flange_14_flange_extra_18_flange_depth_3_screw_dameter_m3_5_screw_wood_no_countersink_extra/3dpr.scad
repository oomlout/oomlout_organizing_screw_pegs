$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -30.0000000000]) {
			cylinder(h = 30, r = 7.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 16.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -30]) {
			cylinder(h = 30, r = 1.8000000000);
		}
	}
}