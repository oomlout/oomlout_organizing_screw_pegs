$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, -3.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										#translate(v = [0, 0, -3.7000000000]) {
											cylinder(h = 3.7000000000, r = 7.5000000000, r1 = 2.0000000000, r2 = 4.9000000000);
										}
										#translate(v = [0, 0, -10.0000000000]) {
											cylinder(h = 10, r = 2.0000000000);
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
			}
		}
	}
	translate(v = [0, 24, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, -0.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										#translate(v = [0, 0, -3.7000000000]) {
											cylinder(h = 3.7000000000, r = 7.5000000000, r1 = 2.0000000000, r2 = 4.9000000000);
										}
										#translate(v = [0, 0, -10.0000000000]) {
											cylinder(h = 10, r = 2.0000000000);
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
			}
		}
	}
	translate(v = [0, 48, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 2.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										#translate(v = [0, 0, -3.7000000000]) {
											cylinder(h = 3.7000000000, r = 7.5000000000, r1 = 2.0000000000, r2 = 4.9000000000);
										}
										#translate(v = [0, 0, -10.0000000000]) {
											cylinder(h = 10, r = 2.0000000000);
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
			}
		}
	}
}