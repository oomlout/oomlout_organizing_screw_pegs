$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -45.0000000000]) {
			cylinder(h = 45, r = 7.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -45]) {
			cylinder(h = 45, r = 2.2500000000);
		}
	}
}