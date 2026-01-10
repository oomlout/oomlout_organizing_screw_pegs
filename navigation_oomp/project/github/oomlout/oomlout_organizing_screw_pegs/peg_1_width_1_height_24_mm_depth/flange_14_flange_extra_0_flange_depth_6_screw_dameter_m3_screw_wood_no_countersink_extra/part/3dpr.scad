$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -24.0000000000]) {
			cylinder(h = 24, r = 7.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -24]) {
			cylinder(h = 24, r = 1.8000000000);
		}
	}
}