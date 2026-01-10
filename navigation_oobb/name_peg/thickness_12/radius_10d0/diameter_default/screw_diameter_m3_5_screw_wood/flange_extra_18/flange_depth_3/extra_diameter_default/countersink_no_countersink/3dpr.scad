$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -12.0000000000]) {
			cylinder(h = 12, r = 10.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 19.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -12]) {
			cylinder(h = 12, r = 1.8000000000);
		}
	}
}