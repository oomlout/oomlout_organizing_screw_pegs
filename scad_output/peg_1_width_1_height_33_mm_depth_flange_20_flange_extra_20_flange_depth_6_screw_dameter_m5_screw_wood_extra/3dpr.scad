$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -33.0000000000]) {
			cylinder(h = 33, r = 10.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 20.0000000000);
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -33.0000000000]) {
							cylinder(h = 33, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.7500000000, r2 = 5.5000000000);
						}
						#translate(v = [0, 0, -33.0000000000]) {
							cylinder(h = 33, r = 2.7500000000);
						}
						#translate(v = [0, 0, -33.0000000000]) {
							cylinder(h = 33, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
	}
}