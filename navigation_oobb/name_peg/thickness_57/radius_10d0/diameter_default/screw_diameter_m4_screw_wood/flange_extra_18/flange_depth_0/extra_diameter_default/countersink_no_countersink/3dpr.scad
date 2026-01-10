$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -57.0000000000]) {
			cylinder(h = 57, r = 10.0000000000);
		}
		cylinder(h = 0, r = 19.0000000000);
	}
	union() {
		#translate(v = [0, 0, -57]) {
			cylinder(h = 57, r = 2.2500000000);
		}
	}
}