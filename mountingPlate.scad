$fn=25;
difference(){
	cube([120,60,5]);
	// pi top
	color([0,1,0]){
	translate([3,3,-1])cylinder(h=10,r=2);
	translate([3,51,-1])cylinder(h=10,r=2);
	translate([61,51,-1])cylinder(h=10,r=2);
	translate([61,3,-1])cylinder(h=10,r=2);
	}
	// pi cam top
	color([1,0,0]){
	translate([117,3,-1])cylinder(h=10,r=1);
	translate([117,23,-1])cylinder(h=10,r=1);
	translate([117-13.2,3,-1])cylinder(h=10,r=1);
	translate([117-13.2,23,-1])cylinder(h=10,r=1);
	}
	// arduino bottom
	color([0,0,1]){
	translate([110,60-17,-1])cylinder(h=10,r=3);
	translate([110-44,60-17,-1])cylinder(h=10,r=3);
	}
	// GPS top
	color([0,0,1]){
	translate([110-32,60-27,3])cube([20,20,6]);
	}
}
