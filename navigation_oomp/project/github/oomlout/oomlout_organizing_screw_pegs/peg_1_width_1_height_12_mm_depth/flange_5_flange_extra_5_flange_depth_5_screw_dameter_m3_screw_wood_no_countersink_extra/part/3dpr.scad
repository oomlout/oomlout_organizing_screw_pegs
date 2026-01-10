$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -12.0000000000]) {
			cylinder(h = 12, r = 2.5000000000);
		}
		translate(v = [0, 0, -5.0000000000]) {
			cylinder(h = 5, r = 5.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -12]) {
			cylinder(h = 12, r = 1.8000000000);
		}
	}
}