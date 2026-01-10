$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -40.0000000000]) {
			cylinder(h = 40, r = 4.0000000000);
		}
		cylinder(h = 0, r = 7.0000000000);
	}
	union() {
		#translate(v = [0, 0, -40]) {
			cylinder(h = 40, r = 2.2500000000);
		}
	}
}