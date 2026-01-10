$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -70.0000000000]) {
			cylinder(h = 70, r = 5.0000000000);
		}
		cylinder(h = 0, r = 8.0000000000);
	}
	union() {
		#translate(v = [0, 0, -70]) {
			cylinder(h = 70, r = 2.2500000000);
		}
	}
}