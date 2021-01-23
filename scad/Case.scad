$fn=25;
height = 28;
depth = 126;
width = 66;
module halfbox(){
	union(){
		difference(){
			cube([depth,width,height]);
			translate([2,2,2.1])cube([depth-4,width-4,height-2]);
		}
	}
	translate([depth-6,0,0])cube([6,6,height-2.7]);
	cube([6,6,height-2.7]);
	translate([2,width-6,0])cube([4,4,height-2.7]);
	translate([depth-30,width-6,0])cube([4,4,height-2.7]);
}

module halfhinge(n,o){
	translate([depth+(o),(width/7)*n,height+1]){
		rotate([90,0,0]){
			difference(){
				cylinder(h=(width/7),r=3);
				color([1,0,0])cylinder(h=10,r=1.75/2);
			}
		}
	}
}
module box(){
	union(){
	halfbox();
	translate([depth+15,0,0]){
	halfbox();}
	halfhinge(1,1);
	halfhinge(2,15);
	halfhinge(3,1);
	halfhinge(4,15);
	halfhinge(5,1);
	halfhinge(6,15);
	halfhinge(7,1);
	}		
}
difference(){	
	box();
	translate([-.1,width/2-.1,height-9.9])cube([5,5,10]);
	translate([depth*2+15-4,width/2-.1,height-9.9])cube([5,5,10]);
	translate([depth-17, width-4.5, height-9.9])cube([15,5,10]);
	translate([2, 2, -.1])cube([20,20,3]);

}



