$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 7.0000000000);
		}
		cylinder(h = 0, r = 10.0000000000);
	}
	union() {
		#translate(v = [0, 0, -6]) {
			cylinder(h = 6, r = 2.2500000000);
		}
	}
}