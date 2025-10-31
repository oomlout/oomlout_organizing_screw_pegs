$fn = 50;


difference() {
	union() {
		cylinder(h = 60, r = 7.0000000000);
		translate(v = [-5.0000000000, 0, 0]) {
			cylinder(h = 60, r = 7.0000000000);
		}
	}
	union() {
		cylinder(h = 60, r = 3.2500000000);
		cylinder(h = 60, r = 1.8000000000);
		cylinder(h = 60, r = 1.8000000000);
		cylinder(h = 60, r = 1.8000000000);
		translate(v = [-9.5000000000, 0, 0]) {
			hull() {
				translate(v = [-3.7500000000, 0.0000000000, 0]) {
					cylinder(h = 60, r = 5.5000000000);
				}
				translate(v = [3.7500000000, 0.0000000000, 0]) {
					cylinder(h = 60, r = 5.5000000000);
				}
				translate(v = [-3.7500000000, -0.0000000000, 0]) {
					cylinder(h = 60, r = 5.5000000000);
				}
				translate(v = [3.7500000000, -0.0000000000, 0]) {
					cylinder(h = 60, r = 5.5000000000);
				}
			}
		}
		translate(v = [-2.0000000000, 0, 0.0000000000]) {
			cylinder(h = 60, r = 8.5000000000);
		}
	}
}