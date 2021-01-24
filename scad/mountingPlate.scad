$fn=25;
module chamfer(x){
	difference(){
		cube([x,x,x]);
		translate([x+.1,x+.1,-.1])cylinder(r=x,h=x+.2);
	}
}	
difference(){
	union(){
		color([0,0,0]){
		cube([120,60,5]); // defien main board

		}
		color([]){
		cube([2,45,9.5]);
		cube([50,2,9.5]);
			}
		}

 // HOLES START HERE
	// pi top
	color([0,1,0]){
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
		}
	// methane bottom
	color([1,1,0]){
	translate([18,30,2.01])cylinder(h=3,r=3.5);
	translate([18,30,-1])cylinder(h=10,r=1.75);
	}
	// GPS top
	color([0,1,1]){
	translate([110-32,60-27,3])cube([18,18,2.1]);
	translate([110-35,60-17,-.1])cylinder(h=3,r=4.2);
	translate([110-35,60-17,-1])cylinder(h=10,r=2);
	translate([110-10,60-17,-.1])cylinder(h=3,r=4.2);
	translate([110-10,60-17,-1])cylinder(h=10,r=2);
	}
	// arduino bottom
	color([0,0,1]){
	translate([110,60-17,2.01])cylinder(h=3,r=3.5);
	translate([110,60-17,-1])cylinder(h=10,r=1.75);
	translate([110-42,60-17,2.01])cylinder(h=3,r=3.5);
	translate([110-42,60-17,-1])cylinder(h=10,r=1.75);
		}
	// BME280 bottom
	color([1,0,1]){
	translate([86-25,10,2.1])cube([25,18,4.5]);
	translate([86-20,11,-.1])cube([20,5,20]);
	translate([90,20,-.1])cylinder(h=3,r=4.2);
	translate([90,20,-1])cylinder(h=10,r=2);
		}
	//MASS REDUCTION HOLES / WIRING ROUTES
	color([.5,.5,.5]){
		translate([110-29.5,60-24.5,-.1])cube([10,10,10]);
		translate([110-20,5.5,-.1])cube([20,20,10]);
		translate([55,35,-.1])chamfer(6);
		translate([30,30,-.1])cube([25.15,20,10]);
		translate([30,10,-.1])cube([40,25.15,10]);
		}
}
		//translate([55,35,-.1])chamfer(6);
//GPS BRACKET
translate([35,13,0]){
	difference([]){
		cube([30,8,7]);
		translate([15-(18/2),-.5,0])color([1,0,0])cube([18,9,6.77-2.1]);
		translate([3,4,4.1])cylinder(h=3,r=3.5);
		translate([3,4,-1])cylinder(h=10,r=1.75);
		translate([30-3,4,4.1])cylinder(h=3,r=3.5);
		translate([30-3,4,-1])cylinder(h=10,r=1.75);
	}
	
	
}

// BME280 mounting plate
translate([35,25,0]){
	difference([]){
		cube([16,8,4]);
		translate([3,4,1.5])cylinder(h=3,r=3.5);
		translate([3,4,-1])cylinder(h=10,r=1.75);
	}
}
difference(){
	color([0,0,0]){
		translate([90,20,0])cylinder(h=5,r=4);
	}
	translate([90,20,-.1])cylinder(h=3,r=4.2);
	translate([90,20,-1])cylinder(h=10,r=2);
	
}