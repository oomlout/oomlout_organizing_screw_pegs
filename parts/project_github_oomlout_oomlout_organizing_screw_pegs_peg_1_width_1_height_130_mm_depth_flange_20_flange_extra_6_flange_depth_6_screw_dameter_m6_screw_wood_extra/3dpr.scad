$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -130.0000000000]) {
			cylinder(h = 130, r = 10.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 13.0000000000);
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -130.0000000000]) {
							cylinder(h = 130, r = 2.2500000000);
						}
						#translate(v = [0, 0, -6]) {
							cylinder(h = 6, r = 10.0000000000, r1 = 3.2500000000, r2 = 6.5000000000);
						}
						#translate(v = [0, 0, -130.0000000000]) {
							cylinder(h = 130, r = 3.2500000000);
						}
						#translate(v = [0, 0, -130.0000000000]) {
							cylinder(h = 130, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
	}
}