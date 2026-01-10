$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -57.0000000000]) {
			cylinder(h = 57, r = 7.0000000000);
		}
		cylinder(h = 0, r = 17.0000000000);
	}
	union() {
		#translate(v = [0, 0, -57]) {
			cylinder(h = 57, r = 2.7500000000);
		}
	}
}