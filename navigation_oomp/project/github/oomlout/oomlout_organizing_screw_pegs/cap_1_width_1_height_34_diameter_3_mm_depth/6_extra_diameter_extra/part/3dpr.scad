$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -4.0000000000]) {
			cylinder(h = 4, r = 20.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 17.1000000000);
		}
	}
}