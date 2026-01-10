$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -39.0000000000]) {
			cylinder(h = 39, r = 7.0000000000);
		}
		cylinder(h = 0, r = 17.0000000000);
	}
	union() {
		#translate(v = [0, 0, -39]) {
			cylinder(h = 39, r = 1.8000000000);
		}
	}
}