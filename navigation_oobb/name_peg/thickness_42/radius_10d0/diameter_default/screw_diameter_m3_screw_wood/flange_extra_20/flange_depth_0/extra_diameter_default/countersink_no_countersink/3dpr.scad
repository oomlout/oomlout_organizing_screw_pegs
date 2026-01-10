$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -42.0000000000]) {
			cylinder(h = 42, r = 10.0000000000);
		}
		cylinder(h = 0, r = 20.0000000000);
	}
	union() {
		#translate(v = [0, 0, -42]) {
			cylinder(h = 42, r = 1.8000000000);
		}
	}
}