$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -40.0000000000]) {
			cylinder(h = 40, r = 10.0000000000);
		}
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 6, r = 60.0000000000);
		}
	}
	union() {
		translate(v = [6.0000000000, 0.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.0000000000);
						}
						#translate(v = [0, 0, -3]) {
							cylinder(h = 3, r = 10.0000000000, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.1250000000);
						}
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.0000000000);
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
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.0000000000);
						}
						#translate(v = [0, 0, -3]) {
							cylinder(h = 3, r = 10.0000000000, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.1250000000);
						}
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.0000000000);
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
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.0000000000);
						}
						#translate(v = [0, 0, -3]) {
							cylinder(h = 3, r = 10.0000000000, r1 = 2.1250000000, r2 = 3.7500000000);
						}
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.1250000000);
						}
						#translate(v = [0, 0, -40.0000000000]) {
							cylinder(h = 40, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
	}
}