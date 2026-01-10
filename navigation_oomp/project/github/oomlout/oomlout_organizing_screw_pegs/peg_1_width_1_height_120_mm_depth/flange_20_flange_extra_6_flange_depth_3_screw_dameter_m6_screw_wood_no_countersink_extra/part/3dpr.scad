$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -120.0000000000]) {
			cylinder(h = 120, r = 10.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 13.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -120]) {
			cylinder(h = 120, r = 3.2500000000);
		}
	}
}