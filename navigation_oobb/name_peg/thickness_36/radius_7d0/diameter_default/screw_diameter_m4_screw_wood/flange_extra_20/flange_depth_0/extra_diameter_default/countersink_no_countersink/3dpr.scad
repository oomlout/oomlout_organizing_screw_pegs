$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -36.0000000000]) {
			cylinder(h = 36, r = 7.0000000000);
		}
		cylinder(h = 0, r = 17.0000000000);
	}
	union() {
		#translate(v = [0, 0, -36]) {
			cylinder(h = 36, r = 2.2500000000);
		}
	}
}