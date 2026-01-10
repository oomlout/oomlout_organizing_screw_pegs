$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -54.0000000000]) {
			cylinder(h = 54, r = 10.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 19.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -54]) {
			cylinder(h = 54, r = 1.8000000000);
		}
	}
}