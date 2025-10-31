$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -54.0000000000]) {
			cylinder(h = 54, r = 7.0000000000);
		}
		cylinder(h = 0, r = 16.0000000000);
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -54.0000000000]) {
							cylinder(h = 54, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r = 7.0000000000, r1 = 2.7500000000, r2 = 5.5000000000);
						}
						#translate(v = [0, 0, -54.0000000000]) {
							cylinder(h = 54, r = 2.7500000000);
						}
						#translate(v = [0, 0, -54.0000000000]) {
							cylinder(h = 54, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
	}
}