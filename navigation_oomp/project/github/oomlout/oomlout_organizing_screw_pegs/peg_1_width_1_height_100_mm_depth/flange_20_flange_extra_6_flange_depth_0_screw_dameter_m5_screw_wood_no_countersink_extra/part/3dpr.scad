$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -100.0000000000]) {
			cylinder(h = 100, r = 10.0000000000);
		}
		cylinder(h = 0, r = 13.0000000000);
	}
	union() {
		#translate(v = [0, 0, -100]) {
			cylinder(h = 100, r = 2.7500000000);
		}
	}
}