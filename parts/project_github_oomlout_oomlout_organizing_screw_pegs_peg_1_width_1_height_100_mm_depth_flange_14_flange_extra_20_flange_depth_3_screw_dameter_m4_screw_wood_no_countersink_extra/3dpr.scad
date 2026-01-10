$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -100.0000000000]) {
			cylinder(h = 100, r = 7.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 17.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -100]) {
			cylinder(h = 100, r = 2.2500000000);
		}
	}
}