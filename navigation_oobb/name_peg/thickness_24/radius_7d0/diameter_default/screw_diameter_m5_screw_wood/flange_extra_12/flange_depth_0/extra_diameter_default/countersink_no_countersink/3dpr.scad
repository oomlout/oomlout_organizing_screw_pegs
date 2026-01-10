$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -24.0000000000]) {
			cylinder(h = 24, r = 7.0000000000);
		}
		cylinder(h = 0, r = 13.0000000000);
	}
	union() {
		#translate(v = [0, 0, -24]) {
			cylinder(h = 24, r = 2.7500000000);
		}
	}
}