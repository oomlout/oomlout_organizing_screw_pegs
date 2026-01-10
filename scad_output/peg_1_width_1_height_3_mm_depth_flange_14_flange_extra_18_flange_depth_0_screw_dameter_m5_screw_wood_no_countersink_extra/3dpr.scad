$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 7.0000000000);
		}
		cylinder(h = 0, r = 16.0000000000);
	}
	union() {
		#translate(v = [0, 0, -3]) {
			cylinder(h = 3, r = 2.7500000000);
		}
	}
}