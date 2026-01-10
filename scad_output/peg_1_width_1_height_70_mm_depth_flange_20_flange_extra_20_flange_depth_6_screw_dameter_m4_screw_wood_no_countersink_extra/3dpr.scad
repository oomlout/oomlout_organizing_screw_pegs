$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -70.0000000000]) {
			cylinder(h = 70, r = 10.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 20.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -70]) {
			cylinder(h = 70, r = 2.2500000000);
		}
	}
}