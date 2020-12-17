#include <Adafruit_GPS.h>
const int VOL_PIN = A0; //(Methane) [CAN BE A0-A7]
//
void setup(){
    Adafruit_GPS GPS(&mySerial);
    Serial.begin( 9600 );
    GPS.begin( 9600 );
    SoftwareSerial myserial(A4, A5) //(GPS) [THESE ARE THE 12c SERIAL PINS]
    //A4 as SDA (serial data) and A5 as SCL (serial clock)
    GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA); // GPS output format
    GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ); // one cycle per second
}
//
void loop(){
  //Start GPS stuff
  GPS.parse(GPS.lastNMEA()); // This splits the last GPS data read into parts
  if (GPS.fix) { //test if gps has a reading
      Serial.print(GPS.latitude, 4); Serial.print(GPS.lat);
      Serial.print(GPS.longitude, 4); Serial.println(GPS.lon);
      //
      Serial.print("Velocity (kn): "); Serial.println(GPS.speed);
      //
      Serial.print(" quality: "); Serial.println((int)GPS.fixquality);
      //
      Serial.print("Altitude: "); Serial.println(GPS.altitude);
    }
}
    // Start Methane stuff
    int value;
    float volt;
//
    value = analogRead( VOL_PIN );
//
    volt = value * 5.0 / 1023.0;
//
    Serial.print( "Value: " );
    Serial.print( value );
    Serial.print( "  Volt: " );
    Serial.println( volt );
}
