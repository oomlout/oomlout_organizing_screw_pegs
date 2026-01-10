$fn = 50;


difference() {
	union() {
		cylinder(h = 0, r = 12.5000000000);
	}
	union() {
		#translate(v = [8.0000000000, 0.0000000000, 0]) {
			cylinder(h = 0, r = 3.2500000000);
		}
		#translate(v = [-4.0000000000, 6.9282032303, 0]) {
			cylinder(h = 0, r = 3.2500000000);
		}
		#translate(v = [-4.0000000000, -6.9282032303, 0]) {
			cylinder(h = 0, r = 3.2500000000);
		}
	}
}