length = 60;
M3 = 1.65; // Hole radius for m3 hardware
SAE6 = 1.80; // Hole radius for 6-32 hardware
difference(){
	union(){
		color([0,0,0]){
		cube([length,60,5]); // defien main board
			}
		}
		{
	color([1,1,0]){ // METHANE
	translate([18,30,-.01])cylinder(h=3,r=3.75);
	translate([18,30,-1])cylinder(h=10,r=SAE6);
	}
	color([0,1,1]){ //GPS
	translate([length-42,60-27,3])cube([19.5,19.5,2.1]);
	translate([length-45,60-17,-.1])cylinder(h=3,r=3.75);
	translate([length-45,60-17,-1])cylinder(h=10,r=SAE6);
	translate([length-20,60-17,-.1])cylinder(h=3,r=3.75);
	translate([length-20,60-17,-1])cylinder(h=10,r=SAE6);
	}
	color([0,0,1]){ //ARDUINO
	translate([length-10,60-17,2.01])cylinder(h=3,r=2.75);
	translate([length-10,60-17,-1])cylinder(h=10,r=M3);
	translate([length-51,60-17,2.01])cylinder(h=3,r=2.75);
	translate([length-51,60-17,-1])cylinder(h=10,r=M3);
		}
	color([1,0,1]){ //BME280
	translate([length-36,10,2.1])cube([27,18,4.5]);
	translate([length-29,11,-.1])cube([20,5,20]);
	translate([length-5,20,-.1])cylinder(h=3,r=3.75);
	translate([length-5,20,-1])cylinder(h=10,r=SAE6);
		}
	color([1,1,0]){// MICRO SD www.adafruit.com/product/254
	translate([10,      25.23,  2.01])cylinder(h=3,r=2.75);
	translate([10,      25.23,  -.01])cylinder(h=10,r=M3);
	translate([10.32+20,5,      2.01])cylinder(h=3,r=2.75);
	translate([10.32+20,5,        -1])cylinder(h=10,r=M3);
	}
		}
	}
translate([100,100,7]){ //GPS BRACKET
	rotate([180,0,0]){
	difference([]){
		cube([20,8,7]);
		translate([15-(18/2),-.5,0])color([1,0,0])cube([18,9,6.77-2.1]);
		translate([3,4,4.1])cylinder(h=3,r=3.75);
		translate([3,4,-1])cylinder(h=10,r=SAE6);
	}
}

}

translate([100,105,0]){ // BME280 mounting plate
	difference([]){
		cube([16,8,4]);
		translate([3,4,1.5])cylinder(h=3,r=3.75);
		translate([3,4,-1])cylinder(h=10,r=SAE6);
	}
}
