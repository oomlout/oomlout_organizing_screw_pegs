$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 7.0000000000);
		}
		cylinder(h = 0, r = 16.0000000000);
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -3.0000000000]) {
							cylinder(h = 3, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r = 7.0000000000, r1 = 2.3750000000, r2 = 4.5000000000);
						}
						#translate(v = [0, 0, -3.0000000000]) {
							cylinder(h = 3, r = 2.3750000000);
						}
						#translate(v = [0, 0, -3.0000000000]) {
							cylinder(h = 3, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
	}
}