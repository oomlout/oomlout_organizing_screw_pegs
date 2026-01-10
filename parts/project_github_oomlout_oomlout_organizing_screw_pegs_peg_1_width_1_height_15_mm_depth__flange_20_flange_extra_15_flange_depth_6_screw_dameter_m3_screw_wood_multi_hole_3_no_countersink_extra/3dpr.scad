$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -15.0000000000]) {
			cylinder(h = 15, r = 10.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 17.5000000000);
		}
	}
	union() {
		#translate(v = [6.0000000000, 0.0000000000, -15]) {
			cylinder(h = 15, r = 1.8000000000);
		}
		#translate(v = [-3.0000000000, 5.1961524227, -15]) {
			cylinder(h = 15, r = 1.8000000000);
		}
		#translate(v = [-3.0000000000, -5.1961524227, -15]) {
			cylinder(h = 15, r = 1.8000000000);
		}
	}
}