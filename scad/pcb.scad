$fn = 25;
length = 60;
M3 = 1.65; // Hole radius for m3 hardware
SAE6 = 1.80; // Hole radius for 6-32 hardware
GPIO = 2.54; // gpio pin spacing
rowtx = 44; // arduino gpio row with tx dist. from edge r
rowvn = 20; // arduino gpio row with vn dist. from edge l.
module trace(p1,p2) {
    color([1,.7,.1]){hull() {
		w = .5;
        translate(p1) cylinder(r=w,h=1.2);
        translate(p2) cylinder(r=w,h=1.2);
    }}
}

difference(){
	union(){
		color([.2,.5,.3]){cube([60,60,1]);}
		}
		{

	color([0,0,1]){ //ARDUINO
	translate([length-10,60-17,-1])cylinder(h=10,r=M3);
	translate([length-51,60-17,-1])cylinder(h=10,r=M3);
		}
	//color([0,1,1]){ //GPS
	//translate([length-45,60-17,-1])cylinder(h=10,r=SAE6);
	//translate([length-20,60-17,-1])cylinder(h=10,r=SAE6);
	//}
	//color([1,0,1]){ //BME280
	//translate([length-36,10,2.1])cube([27,18,4.5]);
	//translate([length-29,11,-.1])cube([20,5,20]);
	//	}
	color([1,1,0]){// MICRO SD www.adafruit.com/product/254
	translate([10,      25.23,  -.01])cylinder(h=10,r=M3);
	translate([20.32+10,    5,    -1])cylinder(h=10,r=M3);
	}
	
	}
}
	
	
	
// TRACES START HERE (FEEL FREE TO CHANGE)
//	color([1,0,0])translate([23,55])cube([5,5,1.5]);
	//color([0,0,0])translate([15,55])cube([5,5,1.5]);
	
	//trace([25.5,55],[25.5,rowtx+2]);//power in to arduino
	//trace([25.5,rowtx+2],[6,rowtx+2]);//power in to arduino
	//trace([6,rowtx+2],[6,60-rowvn]);//power in to arduino
	//trace([6,60-rowvn],[15,60-rowvn]);//power in to arduino
	

	//trace([15.5,55],[15.5,rowtx+5]);//gnd to arduino
	//trace([15.5,rowtx+5],[3,rowtx+5]);//gnd in to arduino
	//trace([3,rowtx+5],[3,60-rowvn-3]);//gnd in to arduino
	//trace([3,60-rowvn-3],[15+GPIO,60-rowvn-3]);//gnd in to arduino
	//trace([15+GPIO,60-rowvn-3],[15+GPIO,60-rowvn]);//gnd in to arduino

	trace([51-(3*GPIO),17],[51-(3*GPIO),13]);//from gas to bme280 SCL
	trace([51-(4*GPIO),17],[51-(4*GPIO),13]);//from gas to bme280   SDA
	trace([51-(5*GPIO),17],[51-(5*GPIO),13]);//from gas to bme280 5v 
	trace([51-(7*GPIO),17],[51-(7*GPIO),13]);//from gas to bme280 gnd

	trace([51-(3*GPIO),55],[51-(3*GPIO),rowtx]);//gps > arduino gnd
	trace([51-(4*GPIO),52],[51-(5*GPIO),rowtx]);//gps > arduino rx
	trace([51-(5*GPIO),51],[51-(15*GPIO),60-rowvn]);//gps > arduino 3.3
	//trace([51-(6*GPIO),rowtx],[51-(5*GPIO),51]);//gps > arduino 3.3
	
	for ( i = [1:1:6]) {
	trace([10,24.23-(i*GPIO)],[13,24.23-(i*GPIO)]);//SD > Arduino
	trace([13,24.23-(i*GPIO)],[17+(i*2),24.23-(i*GPIO)]);//SD > Ar.
	trace([17+(i*2),24.23-(i*GPIO)],[17+(i*2),60-rowvn]);//SD > Ar.
		}
	trace([17+(1*2),60-rowvn],[5,30]); //SD GRD
	trace([5,30],[5,55]); //SD GRD
	trace([5,55],[51-(3*GPIO),55]); //SD GRD
		
	trace([17+(2*2),60-rowvn],[17+(2*2),63.5-rowvn]); //SD 3.3
