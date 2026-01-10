$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -21.0000000000]) {
			cylinder(h = 21, r = 10.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 16.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -21]) {
			cylinder(h = 21, r = 2.2500000000);
		}
	}
}