$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -120.0000000000]) {
			cylinder(h = 120, r = 10.0000000000);
		}
		translate(v = [0, 0, -3.0000000000]) {
			cylinder(h = 3, r = 16.0000000000);
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -120.0000000000]) {
							cylinder(h = 120, r = 2.2500000000);
						}
						#translate(v = [0, 0, -6]) {
							cylinder(h = 6, r1 = 3.2500000000, r2 = 6.5000000000);
						}
						#translate(v = [0, 0, -120.0000000000]) {
							cylinder(h = 120, r = 3.2500000000);
						}
						#translate(v = [0, 0, -120.0000000000]) {
							cylinder(h = 120, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
	}
}