$fn = 50;


difference() {
	union() {
		cylinder(h = 21, r = 7.0000000000);
		translate(v = [-14.0000000000, 0, 0]) {
			cylinder(h = 21, r = 7.0000000000);
		}
	}
	union() {
		cylinder(h = 21, r = 3.2500000000);
		cylinder(h = 21, r = 1.8000000000);
		cylinder(h = 21, r = 1.8000000000);
		cylinder(h = 21, r = 1.8000000000);
		translate(v = [-18.5000000000, 0, 0]) {
			hull() {
				translate(v = [-3.7500000000, 0.0000000000, 0]) {
					cylinder(h = 21, r = 7.5000000000);
				}
				translate(v = [3.7500000000, 0.0000000000, 0]) {
					cylinder(h = 21, r = 7.5000000000);
				}
				translate(v = [-3.7500000000, -0.0000000000, 0]) {
					cylinder(h = 21, r = 7.5000000000);
				}
				translate(v = [3.7500000000, -0.0000000000, 0]) {
					cylinder(h = 21, r = 7.5000000000);
				}
			}
		}
		translate(v = [-11.0000000000, 0, 0.0000000000]) {
			cylinder(h = 21, r = 17.5000000000);
		}
	}
}