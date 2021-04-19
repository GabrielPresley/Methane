/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|*   for grad 2021 BSS SRM Class   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
//              MOSI  MISO  SCK CS
//Arduino Nano  11    12    13  10
#include <Wire.h>
#include <SD.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
//
#define Addr 0x50
//
#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10
#define SEALEVELPRESSURE_HPA (1004.39)
Adafruit_BME280 bme;
//SD Card
const int chipSelect = 10;
//
void setup()
{
  // set baud rate = 9600
  Serial.begin(9600);
  while (!Serial) {} // wait for serial port to connect.
  Wire.begin();  // open I2C comm. as master


  //Adafruit_BME280
  bool status = bme.begin();
  delay(300);


  // Micro Sd adapter
  pinMode(10, OUTPUT);
  if (!SD.begin(chipSelect)) {
   Serial.println("Card having a boomer moment");
   while (1){ //Just set pin 1 high, low a bunch for when no serial port is available
     int PIN = 2;
     pinMode(PIN, OUTPUT);
     digitalWrite(PIN, HIGH);
     delay(500);
     digitalWrite(PIN, LOW);
     delay(500);
   }
  }
  File dataFile = SD.open("output.csv", FILE_WRITE);
  Serial.println("card initialized.");
  dataFile.println("Methane:+");
  dataFile.println("Temperature:@");
  dataFile.println("Pressure:#");
  dataFile.println("Altitude:%");
  dataFile.println("Humidity:&");
  dataFile.close();
}
//
void loop(){
//
  File dataFile = SD.open("output.csv", FILE_WRITE);
  // start I2C
  Wire.beginTransmission(Addr);
  // data register
  Wire.write(0x00);
  // stop I2C transmission
  Wire.endTransmission();
  //
  // request 2 bytes
  Wire.requestFrom(Addr, 2);
  //
  // read 2 bytes
  unsigned int data[2];
  if(Wire.available() == 2)
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
  }
  //
  // make 12-bits
  int raw_adc = ((data[0] & 0x0F) * 256) + data[1];
  float ppm = (10000.0 / 4096.0) * raw_adc + 200.0;

//
  // output
  dataFile.println(); // fixed methane data at end of gps :/
  dataFile.print("+");
  dataFile.println(ppm);
  delay(500);
  //
  dataFile.print("@");
  dataFile.println(bme.readTemperature());
  //
  delay(500);
  dataFile.print("#");
  dataFile.println(bme.readPressure() / 100.0F);
  //
  delay(500);
  dataFile.print("%");
  dataFile.println(bme.readAltitude(SEALEVELPRESSURE_HPA));
  //
  delay(500);
  dataFile.print(":");
  dataFile.println(millis()/1000);
  //
  delay(500);
  dataFile.print("&");
  dataFile.println(bme.readHumidity());
  //
  Serial.println("phase 1");
  while(!Serial.available()){} // wait for serial availablity
  Serial.println("phase 2");
  bool cont = true;
  char prev[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
  char test[] = {'$', 'G', 'P', 'G', 'L', 'L'};
  
  while(cont) // Check for availablity of data at Serial Port
    {

      char data = Serial.read(); // Reading Serial Data and saving in data variable

      Serial.print(data);

      int match = 0;
      for(int i = 0; i < 6; i++){
        if(i > 4){
          prev[i] = data;
        }else{
          prev[i] = prev[i+1];
        }

        if(prev[i] == test[i]){
          match++;
        }
      }

      
      if(match == 6){
        break;
      }
      
      if(data == 0x0A or data == 0x00){
        Serial.println(match);
      }else{
        dataFile.print(data);
      }
            
    }

    Serial.flush();
dataFile.close();
}
