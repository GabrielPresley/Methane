bat_h = 10; // Battery height
bat_w = 30; // Battery width
bat_l = 10; // Amount of extra cover for the battery

bod_d = 40; // Diameter of drone body

$fn = 100;  // Number of sides on a circle

E = 1;      // Modify the length

r  = bat_w * E;
difference(){
	scale([1, .8, 1]){
		rotate_extrude(){
			intersection(){
				difference(){
					square([bat_w,r+1]);
						translate([bat_w/2-r-1+5,-1])
					circle(r);
				}
				translate([bat_w/2-r+5,0])
					circle(r);
			}
			translate([bat_w/2-1+5,-bat_l])square([1,bat_l]);
		}
	}
	translate([0,bod_d/2,-20-bat_l]){
		cylinder(r = bod_d/2, h = 100+bat_l);
	}
}
//translate([-30/2,-bat_h,-10])cube([30,bat_h,10]);
//	translate([0,bod_d/2,-20]){
//		cylinder(r = bod_d/2, h = 100);
//	}
translate([-(bat_w-10)/2,-(bod_d/2-6),-bat_l]){
	cube([bat_w-10,2,bat_l]);
}