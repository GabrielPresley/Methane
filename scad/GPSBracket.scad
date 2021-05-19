w = 18.3; //18.3
d = 8; //8

cube([42+d,w+4,1.5]);
difference(){
	cube([d+2,w+4,w+4]);
	
	translate([2,2,2]){
		cube([d,w,w]);
	}
	
	translate([d/2+2,w/2-1.5,0]){
		cube([d/2,7,60+w]);
	}
	
	translate([-1,(w+4)/2,(w+4)/2])rotate([0,90,0]){
		cylinder(r=w/2.2,h=5);
	}
}
