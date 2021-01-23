$fn=25;
module chamfer(x){
	difference(){
		cube([x,x,x]);
		translate([x+.1,x+.1,-.1])cylinder(r=x,h=x+.2);
	}
}	
difference(){

	color([0,0,0]){
	cube([120,60,5]); // defien main board
			}

 // HOLES START HERE
	// pi top
	color([0,1,0]){
	translate([3,3,-.01])cylinder(h=3,r=2.75);
	translate([3,3,-1])cylinder(h=10,r=1.5);
	translate([3,51,-.01])cylinder(h=3,r=2.75);
	translate([3,51,-1])cylinder(h=10,r=1.5);
	translate([61,51,-.01])cylinder(h=3,r=2.75);
	translate([61,51,-1])cylinder(h=10,r=1.5);
	translate([61,3,-.01])cylinder(h=3,r=2.75);
	translate([61,3,-1])cylinder(h=10,r=1.5);
		}
	// pi cam top
	color([1,0,0]){
	translate([117,3,-.01])cylinder(h=3,r=2.75);
	translate([117,3,-1])cylinder(h=10,r=1.5);
	translate([117,23,-.01])cylinder(h=3,r=2.75);
	translate([117,23,-1])cylinder(h=10,r=1.5);
	translate([117-13.2,3,-.01])cylinder(h=3,r=2.75);
	translate([117-13.2,3,-1])cylinder(h=10,r=1.5);
	translate([117-13.2,23,-.01])cylinder(h=3,r=2.75);
	translate([117-13.2,23,-1])cylinder(h=10,r=1.5);
		}
	// methane bottom
	color([1,1,0]){
	translate([30,30,2.01])cylinder(h=3,r=3.5);
	translate([30,30,-1])cylinder(h=10,r=1.75);
	}
	// GPS top
	color([0,1,1]){
	translate([110-32,60-27,3])cube([20,20,6]);
	}
	// arduino bottom
	color([0,0,1]){
	translate([110,60-17,2.01])cylinder(h=3,r=3.5);
	translate([110,60-17,-1])cylinder(h=10,r=1.75);
	translate([110-44,60-17,2.01])cylinder(h=3,r=3.5);
	translate([110-44,60-17,-1])cylinder(h=10,r=1.75);
		}
	// BME280 bottom
	color([1,0,1]){
	translate([80,10,2.01])cylinder(h=3,r=3.5);
	translate([80,10,-1])cylinder(h=10,r=1.75);
	translate([80,20,2.01])cylinder(h=3,r=3.5);
	translate([80,20,-1])cylinder(h=10,r=1.75);
		}
	//MASS REDUCTION HOLES / WIRING ROUTES
	color([.5,.5,.5]){
		translate([10,10,-.1])cube([10,35,10]);
		translate([110-29.5,60-24.5,-.1])cube([15,15,10]);
		translate([110-20,5.5,-.1])cube([5,5,10]);
		translate([55,35,-.1])chamfer(6);
		translate([40,30,-.1])cube([15.15,20,10]);
		translate([40,10,-.1])cube([30,25.15,10]);
		}
}
		//translate([55,35,-.1])chamfer(6);
