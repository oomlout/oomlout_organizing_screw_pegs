$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -70.0000000000]) {
			cylinder(h = 70, r = 7.0000000000);
		}
		cylinder(h = 0, r = 10.0000000000);
	}
	union() {
		#translate(v = [0, 0, -70]) {
			cylinder(h = 70, r = 1.8000000000);
		}
	}
}