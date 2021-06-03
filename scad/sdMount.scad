w = 26; // width of sdcard board
m0 = 4; // modifier added to width (to make outer size)

d = 42;  // depth of sdcard board
m1 = 10; // modifier added to depth (to make space for shim)

h = 1.5; // methane board pcb thickness
m2 = 2;  // modifier added to height (to make outer size)

shim = .350;
m3 = 3;      //Diameter of m3 screw

$fn = 25; //Set # of sides on a cylinder
difference(){
	cube([w+m0,d+m1,h+m2]); //outer most cube
	
	//PCB slot
	color([1,0,0])translate([2,-.1,(m2)/2])cube([w,d+.1,h]);
	
	//Clearance for the electronics
	color([0,1,0])translate([3,3,-.1])cube([w-2,d-4,h+m2+.2]);
	
	//Opening the front up
	color([0,0,1])translate([2,-.1,m2+.1/2])cube([w,3+.2,m2+1]);
	
	//Shim hole
	translate([m0/2,d-.1,(h+2-shim)/2]){
		color([0,1,1])cube([w,w+m0+.2,shim]);
	}
	
	//Set screw hole to hold shim
	translate([(w+m0)/2,d+(m1/2),-.1]){
		cylinder(r = m3/2, h = h+m2+.2);
	}
}
