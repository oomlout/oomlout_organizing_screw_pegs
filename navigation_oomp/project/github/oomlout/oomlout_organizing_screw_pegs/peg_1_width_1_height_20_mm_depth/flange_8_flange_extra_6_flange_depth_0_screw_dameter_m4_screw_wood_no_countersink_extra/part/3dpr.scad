$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -20.0000000000]) {
			cylinder(h = 20, r = 4.0000000000);
		}
		cylinder(h = 0, r = 7.0000000000);
	}
	union() {
		#translate(v = [0, 0, -20]) {
			cylinder(h = 20, r = 2.2500000000);
		}
	}
}