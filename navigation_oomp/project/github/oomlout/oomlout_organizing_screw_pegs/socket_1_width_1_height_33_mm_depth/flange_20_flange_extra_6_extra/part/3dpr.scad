$fn = 50;


difference() {
	union() {
		cylinder(h = 33, r = 7.0000000000);
		translate(v = [-10.0000000000, 0, 0]) {
			cylinder(h = 33, r = 7.0000000000);
		}
	}
	union() {
		cylinder(h = 33, r = 3.2500000000);
		cylinder(h = 33, r = 1.8000000000);
		cylinder(h = 33, r = 1.8000000000);
		cylinder(h = 33, r = 1.8000000000);
		translate(v = [-14.5000000000, 0, 0]) {
			hull() {
				translate(v = [-3.7500000000, 0.0000000000, 0]) {
					cylinder(h = 33, r = 10.5000000000);
				}
				translate(v = [3.7500000000, 0.0000000000, 0]) {
					cylinder(h = 33, r = 10.5000000000);
				}
				translate(v = [-3.7500000000, -0.0000000000, 0]) {
					cylinder(h = 33, r = 10.5000000000);
				}
				translate(v = [3.7500000000, -0.0000000000, 0]) {
					cylinder(h = 33, r = 10.5000000000);
				}
			}
		}
		translate(v = [-7.0000000000, 0, 0.0000000000]) {
			cylinder(h = 33, r = 13.5000000000);
		}
	}
}