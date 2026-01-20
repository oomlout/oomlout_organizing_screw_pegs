$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -42.0000000000]) {
			cylinder(h = 42, r = 7.0000000000);
		}
		cylinder(h = 0, r = 13.0000000000);
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -42.0000000000]) {
							cylinder(h = 42, r = 2.0000000000);
						}
						#translate(v = [0, 0, -3]) {
							cylinder(h = 3, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						#translate(v = [0, 0, -42.0000000000]) {
							cylinder(h = 42, r = 2.1250000000);
						}
						#translate(v = [0, 0, -42.0000000000]) {
							cylinder(h = 42, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
	}
}