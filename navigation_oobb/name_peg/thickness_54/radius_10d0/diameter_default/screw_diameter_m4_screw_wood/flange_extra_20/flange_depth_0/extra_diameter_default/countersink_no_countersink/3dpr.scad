$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -54.0000000000]) {
			cylinder(h = 54, r = 10.0000000000);
		}
		cylinder(h = 0, r = 20.0000000000);
	}
	union() {
		#translate(v = [0, 0, -54]) {
			cylinder(h = 54, r = 2.2500000000);
		}
	}
}