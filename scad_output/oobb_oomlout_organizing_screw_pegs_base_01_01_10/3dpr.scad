$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -10.0000000000]) {
							cylinder(h = 10, r = 2.0000000000);
						}
						#translate(v = [0, 0, -3.9000000000]) {
							cylinder(h = 3.9000000000, r = 7.5000000000, r1 = 2.2500000000, r2 = 6.1000000000);
						}
						#translate(v = [0, 0, -10.0000000000]) {
							cylinder(h = 10, r = 2.2500000000);
						}
						#translate(v = [0, 0, -10.0000000000]) {
							cylinder(h = 10, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, -10.0000000000]) {
			cylinder(h = 10, r = 7.5000000000);
		}
	}
	union();
}