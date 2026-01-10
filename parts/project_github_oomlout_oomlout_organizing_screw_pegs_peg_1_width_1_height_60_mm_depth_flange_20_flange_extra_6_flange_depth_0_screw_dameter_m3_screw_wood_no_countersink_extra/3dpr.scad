$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -60.0000000000]) {
			cylinder(h = 60, r = 10.0000000000);
		}
		cylinder(h = 0, r = 13.0000000000);
	}
	union() {
		#translate(v = [0, 0, -60]) {
			cylinder(h = 60, r = 1.8000000000);
		}
	}
}