$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -4.0000000000]) {
			cylinder(h = 4, r = 5.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 4.1000000000);
		}
	}
}