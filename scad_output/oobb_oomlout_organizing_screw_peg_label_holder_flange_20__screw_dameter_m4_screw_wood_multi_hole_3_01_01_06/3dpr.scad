$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 3, r = 10.0000000000);
		}
		translate(v = [0, 25.0000000000, -6]) {
			hull() {
				translate(v = [-17.0000000000, 9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [17.0000000000, 9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [-17.0000000000, -9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [17.0000000000, -9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
			}
		}
		translate(v = [0, 7.5000000000, -6]) {
			hull() {
				translate(v = [-9.5000000000, 17.0000000000, 0]) {
					cylinder(h = 3, r = 5);
				}
				translate(v = [9.5000000000, 17.0000000000, 0]) {
					cylinder(h = 3, r = 5);
				}
				translate(v = [-9.5000000000, -17.0000000000, 0]) {
					cylinder(h = 3, r = 5);
				}
				translate(v = [9.5000000000, -17.0000000000, 0]) {
					cylinder(h = 3, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [0, 32.5000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -50.0000000000]) {
							cylinder(h = 100, r = 3.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 32.5000000000, -6]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#linear_extrude(height = 5) {
							polygon(points = [[5.9142500000, 0.0000000000], [2.9571250000, 5.1218907443], [-2.9571250000, 5.1218907443], [-5.9142500000, 0.0000000000], [-2.9571250000, -5.1218907443], [2.9571250000, -5.1218907443]]);
						}
					}
					union();
				}
			}
		}
		translate(v = [6.0000000000, 0.0000000000, 44]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.6000000000);
						}
						translate(v = [0, 0, -3.9000000000]) {
							cylinder(h = 3.9000000000, r1 = 2.8750000000, r2 = 5.4000000000);
						}
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.8750000000);
						}
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.6000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-3.0000000000, 5.1961524227, 44]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.6000000000);
						}
						translate(v = [0, 0, -3.9000000000]) {
							cylinder(h = 3.9000000000, r1 = 2.8750000000, r2 = 5.4000000000);
						}
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.8750000000);
						}
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.6000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-3.0000000000, -5.1961524227, 44]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.6000000000);
						}
						translate(v = [0, 0, -3.9000000000]) {
							cylinder(h = 3.9000000000, r1 = 2.8750000000, r2 = 5.4000000000);
						}
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.8750000000);
						}
						translate(v = [0, 0, -56.0000000000]) {
							cylinder(h = 56, r = 2.6000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-15.0000000000, 17.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [-15.0000000000, 32.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [0.0000000000, 17.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [0.0000000000, 32.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [15.0000000000, 17.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [15.0000000000, 32.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [-15.0000000000, 17.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [-15.0000000000, 25.0000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [-15.0000000000, 32.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [-7.5000000000, 17.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [-7.5000000000, 25.0000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [-7.5000000000, 32.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [0.0000000000, 17.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [0.0000000000, 25.0000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [0.0000000000, 32.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [7.5000000000, 17.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [7.5000000000, 25.0000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [7.5000000000, 32.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [15.0000000000, 17.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [15.0000000000, 25.0000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
		translate(v = [15.0000000000, 32.5000000000, -6]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 1.8000000000);
			}
		}
	}
}