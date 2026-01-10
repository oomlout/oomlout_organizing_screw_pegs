$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -12.0000000000]) {
			cylinder(h = 12, r = 7.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 17.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -12]) {
			cylinder(h = 12, r = 1.8000000000);
		}
	}
}