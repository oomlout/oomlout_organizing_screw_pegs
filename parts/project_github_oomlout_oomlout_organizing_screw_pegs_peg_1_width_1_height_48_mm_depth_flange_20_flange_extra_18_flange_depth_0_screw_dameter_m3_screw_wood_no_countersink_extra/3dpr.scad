$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -48.0000000000]) {
			cylinder(h = 48, r = 10.0000000000);
		}
		cylinder(h = 0, r = 19.0000000000);
	}
	union() {
		#translate(v = [0, 0, -48]) {
			cylinder(h = 48, r = 1.8000000000);
		}
	}
}