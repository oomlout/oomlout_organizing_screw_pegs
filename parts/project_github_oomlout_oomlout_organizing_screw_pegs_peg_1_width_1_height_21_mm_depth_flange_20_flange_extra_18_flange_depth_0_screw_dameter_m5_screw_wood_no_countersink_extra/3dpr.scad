$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -21.0000000000]) {
			cylinder(h = 21, r = 10.0000000000);
		}
		cylinder(h = 0, r = 19.0000000000);
	}
	union() {
		#translate(v = [0, 0, -21]) {
			cylinder(h = 21, r = 2.7500000000);
		}
	}
}