$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -30.0000000000]) {
			cylinder(h = 30, r = 10.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 17.5000000000);
		}
	}
	union() {
		translate(v = [6.0000000000, 0.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r = 10.0000000000, r1 = 2.6000000000, r2 = 4.9000000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.6000000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.8750000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.6000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-3.0000000000, 5.1961524227, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r = 10.0000000000, r1 = 2.6000000000, r2 = 4.9000000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.6000000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.8750000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.6000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-3.0000000000, -5.1961524227, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r = 10.0000000000, r1 = 2.6000000000, r2 = 4.9000000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.6000000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.8750000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 2.6000000000);
						}
					}
					union();
				}
			}
		}
	}
}