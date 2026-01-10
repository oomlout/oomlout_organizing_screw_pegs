$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -75.0000000000]) {
			cylinder(h = 75, r = 12.5000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 62.5000000000);
		}
	}
	union() {
		#translate(v = [8.0000000000, 0.0000000000, -75]) {
			cylinder(h = 75, r = 3.2500000000);
		}
		#translate(v = [-4.0000000000, 6.9282032303, -75]) {
			cylinder(h = 75, r = 3.2500000000);
		}
		#translate(v = [-4.0000000000, -6.9282032303, -75]) {
			cylinder(h = 75, r = 3.2500000000);
		}
	}
}