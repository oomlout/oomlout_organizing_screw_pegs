$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -24.0000000000]) {
			cylinder(h = 24, r = 10.0000000000);
		}
		cylinder(h = 0, r = 19.0000000000);
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -24.0000000000]) {
							cylinder(h = 24, r = 2.6000000000);
						}
						#translate(v = [0, 0, -3.9000000000]) {
							cylinder(h = 3.9000000000, r = 10.0000000000, r1 = 2.8750000000, r2 = 5.4000000000);
						}
						#translate(v = [0, 0, -24.0000000000]) {
							cylinder(h = 24, r = 2.8750000000);
						}
						#translate(v = [0, 0, -24.0000000000]) {
							cylinder(h = 24, r = 2.6000000000);
						}
					}
					union();
				}
			}
		}
	}
}