$fn = 50;


difference() {
	union() {
		cylinder(h = 12, r = 7.0000000000);
		translate(v = [-2.0000000000, 0, 0]) {
			cylinder(h = 12, r = 7.0000000000);
		}
	}
	union() {
		cylinder(h = 12, r = 3.2500000000);
		cylinder(h = 12, r = 1.8000000000);
		cylinder(h = 12, r = 1.8000000000);
		cylinder(h = 12, r = 1.8000000000);
		translate(v = [-6.5000000000, 0, 0]) {
			hull() {
				translate(v = [-3.7500000000, 0.0000000000, 0]) {
					cylinder(h = 12, r = 3.0000000000);
				}
				translate(v = [3.7500000000, 0.0000000000, 0]) {
					cylinder(h = 12, r = 3.0000000000);
				}
				translate(v = [-3.7500000000, -0.0000000000, 0]) {
					cylinder(h = 12, r = 3.0000000000);
				}
				translate(v = [3.7500000000, -0.0000000000, 0]) {
					cylinder(h = 12, r = 3.0000000000);
				}
			}
		}
		translate(v = [1.0000000000, 0, 0.0000000000]) {
			cylinder(h = 12, r = 5.5000000000);
		}
	}
}