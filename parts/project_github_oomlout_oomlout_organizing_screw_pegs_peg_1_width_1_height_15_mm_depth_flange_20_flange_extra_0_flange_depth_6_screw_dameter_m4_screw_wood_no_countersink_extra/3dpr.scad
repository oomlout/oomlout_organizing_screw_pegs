$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -15.0000000000]) {
			cylinder(h = 15, r = 10.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -15]) {
			cylinder(h = 15, r = 2.2500000000);
		}
	}
}