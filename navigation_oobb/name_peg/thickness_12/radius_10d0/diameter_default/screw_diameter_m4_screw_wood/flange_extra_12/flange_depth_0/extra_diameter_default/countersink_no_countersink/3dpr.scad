$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -12.0000000000]) {
			cylinder(h = 12, r = 10.0000000000);
		}
		cylinder(h = 0, r = 16.0000000000);
	}
	union() {
		#translate(v = [0, 0, -12]) {
			cylinder(h = 12, r = 2.2500000000);
		}
	}
}