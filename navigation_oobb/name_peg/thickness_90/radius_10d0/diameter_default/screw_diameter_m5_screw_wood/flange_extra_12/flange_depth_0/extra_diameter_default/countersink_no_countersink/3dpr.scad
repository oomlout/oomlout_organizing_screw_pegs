$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -90.0000000000]) {
			cylinder(h = 90, r = 10.0000000000);
		}
		cylinder(h = 0, r = 16.0000000000);
	}
	union() {
		#translate(v = [0, 0, -90]) {
			cylinder(h = 90, r = 2.7500000000);
		}
	}
}