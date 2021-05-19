w = 26;
d = 42;
h = 1.5;

difference(){
	cube([w+4,d+4,h+2]);
	color([1,0,0])translate([2,-.1,1])cube([w,d+.1,h]);
	color([0,1,0])translate([3,3,-.1])cube([w-2,d-4,h+2.2]);
	color([0,0,1])translate([2,-.1,2])cube([w,3+.2,2]);
}
translate([0,d+4,0]){
	color([0,1,1])cube([w+4,w+4,1.5]);
}