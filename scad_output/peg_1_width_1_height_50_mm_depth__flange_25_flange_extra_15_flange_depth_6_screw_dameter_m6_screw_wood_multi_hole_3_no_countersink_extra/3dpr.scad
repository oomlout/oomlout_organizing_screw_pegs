$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -50.0000000000]) {
			cylinder(h = 50, r = 12.5000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 20.0000000000);
		}
	}
	union() {
		translate(v = [8.0000000000, 0.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 2.2500000000);
						}
						#translate(v = [0, 0, -6]) {
							cylinder(h = 6, r = 12.5000000000, r1 = 3.2500000000, r2 = 6.5000000000);
						}
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 3.2500000000);
						}
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-4.0000000000, 6.9282032303, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 2.2500000000);
						}
						#translate(v = [0, 0, -6]) {
							cylinder(h = 6, r = 12.5000000000, r1 = 3.2500000000, r2 = 6.5000000000);
						}
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 3.2500000000);
						}
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-4.0000000000, -6.9282032303, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 2.2500000000);
						}
						#translate(v = [0, 0, -6]) {
							cylinder(h = 6, r = 12.5000000000, r1 = 3.2500000000, r2 = 6.5000000000);
						}
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 3.2500000000);
						}
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 50, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
	}
}