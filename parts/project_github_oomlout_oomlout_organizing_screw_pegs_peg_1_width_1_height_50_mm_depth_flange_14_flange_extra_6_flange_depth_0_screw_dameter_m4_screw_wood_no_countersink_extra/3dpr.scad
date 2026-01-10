$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -50.0000000000]) {
			cylinder(h = 50, r = 7.0000000000);
		}
		cylinder(h = 0, r = 10.0000000000);
	}
	union() {
		#translate(v = [0, 0, -50]) {
			cylinder(h = 50, r = 2.2500000000);
		}
	}
}