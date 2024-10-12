$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, -6.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -15]) {
							hull() {
								translate(v = [-5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [-5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
							}
						}
						translate(v = [0, 0, -3]) {
							hull() {
								translate(v = [-8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [-8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
							}
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										#translate(v = [0, 0, -3.7000000000]) {
											cylinder(h = 3.7000000000, r = 10.0000000000, r1 = 2.6000000000, r2 = 4.9000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.8750000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
									}
									union();
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0, 24, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, -3.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -15]) {
							hull() {
								translate(v = [-5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [-5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
							}
						}
						translate(v = [0, 0, -3]) {
							hull() {
								translate(v = [-8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [-8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
							}
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										#translate(v = [0, 0, -3.7000000000]) {
											cylinder(h = 3.7000000000, r = 10.0000000000, r1 = 2.6000000000, r2 = 4.9000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.8750000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
									}
									union();
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0, 48, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 0.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -15]) {
							hull() {
								translate(v = [-5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [-5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
							}
						}
						translate(v = [0, 0, -3]) {
							hull() {
								translate(v = [-8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [-8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
							}
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										#translate(v = [0, 0, -3.7000000000]) {
											cylinder(h = 3.7000000000, r = 10.0000000000, r1 = 2.6000000000, r2 = 4.9000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.8750000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
									}
									union();
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0, 72, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 3.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -15]) {
							hull() {
								translate(v = [-5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [-5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
							}
						}
						translate(v = [0, 0, -3]) {
							hull() {
								translate(v = [-8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [-8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
							}
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										#translate(v = [0, 0, -3.7000000000]) {
											cylinder(h = 3.7000000000, r = 10.0000000000, r1 = 2.6000000000, r2 = 4.9000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.8750000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
									}
									union();
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0, 96, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 6.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, -15]) {
							hull() {
								translate(v = [-5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, 0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [-5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
								translate(v = [5.0000000000, -0.0000000000, 0]) {
									cylinder(h = 15, r = 10.0000000000);
								}
							}
						}
						translate(v = [0, 0, -3]) {
							hull() {
								translate(v = [-8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, 3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [-8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
								translate(v = [8.0000000000, -3.0000000000, 0]) {
									cylinder(h = 3, r = 10.0000000000);
								}
							}
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										#translate(v = [0, 0, -3.7000000000]) {
											cylinder(h = 3.7000000000, r = 10.0000000000, r1 = 2.6000000000, r2 = 4.9000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.8750000000);
										}
										#translate(v = [0, 0, -15.0000000000]) {
											cylinder(h = 15, r = 2.6000000000);
										}
									}
									union();
								}
							}
						}
					}
				}
			}
		}
	}
}