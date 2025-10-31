$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -7.0000000000]) {
			cylinder(h = 7, r = 18.5000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 12.6000000000);
		}
	}
}