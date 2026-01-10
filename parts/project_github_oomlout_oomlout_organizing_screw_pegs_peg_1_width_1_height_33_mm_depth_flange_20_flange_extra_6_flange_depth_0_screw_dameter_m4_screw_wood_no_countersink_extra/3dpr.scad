$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -33.0000000000]) {
			cylinder(h = 33, r = 10.0000000000);
		}
		cylinder(h = 0, r = 13.0000000000);
	}
	union() {
		#translate(v = [0, 0, -33]) {
			cylinder(h = 33, r = 2.2500000000);
		}
	}
}