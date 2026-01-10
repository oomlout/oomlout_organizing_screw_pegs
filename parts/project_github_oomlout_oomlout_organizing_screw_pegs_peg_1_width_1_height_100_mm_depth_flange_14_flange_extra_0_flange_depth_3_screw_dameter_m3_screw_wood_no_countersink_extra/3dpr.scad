$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -100.0000000000]) {
			cylinder(h = 100, r = 7.0000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -100]) {
			cylinder(h = 100, r = 1.8000000000);
		}
	}
}