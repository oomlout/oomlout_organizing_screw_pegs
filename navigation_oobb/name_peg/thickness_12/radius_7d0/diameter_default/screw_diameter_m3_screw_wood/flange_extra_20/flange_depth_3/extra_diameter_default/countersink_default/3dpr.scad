$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -12.0000000000]) {
			cylinder(h = 12, r = 7.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 17.0000000000);
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
						#translate(v = [0, 0, -3]) {
							cylinder(h = 3, r = 7.0000000000, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.1250000000);
						}
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
	}
}