$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -25.0000000000]) {
			cylinder(h = 25, r = 12.5000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 18.5000000000);
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r = 12.5000000000, r1 = 2.6000000000, r2 = 4.9000000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.6000000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.8750000000);
						}
						translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 2.6000000000);
						}
					}
					union();
				}
			}
		}
	}
}