/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|*   for grad 2021 BSS SRM Class   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
//
//
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
//
// address is 0x50
// This is according to the example code in the
// wire library i2c_scanner
#define Addr 0x50
//Adafruit_BME280
#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10
#define SEALEVELPRESSURE_HPA (1013.25)
Adafruit_BME280 bme;
//
void setup()
{
  // open I2C comm. as master
  Wire.begin();
  // set baud rate = 9600
  Serial.begin(9600); //you initialized the serial port twice
  //Adafruit_BME280
  bool status;
  status = bme.begin();
  delay(300);
  // GPS
  Serial.begin(9600); // Serial Port initialization
}
//
void loop()
{
//
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
  Serial.print("Methane (PPM) ");
  Serial.println(ppm);
  delay(500);
  //
  Serial.print("Temperature (*c) ");
  Serial.println(bme.readTemperature());
  //
  delay(500);
  Serial.print("Pressure (hPa) ");
  Serial.println(bme.readPressure() / 100.0F);
  //
  delay(500);
  Serial.print("Altitude (m) ");
  Serial.println(bme.readAltitude(SEALEVELPRESSURE_HPA));
  //
  delay(500);
  Serial.println();
  Serial.print("Humidity (%) ");
  Serial.println(bme.readHumidity());
  //
  while(Serial.available()) // Chek for availablity of data at Serial Port
    {
      char data = Serial.read(); // Reading Serial Data and saving in data variable
      Serial.print(data);
      if(data == "$"){
        char data = Serial.read();
          if(data == "G"){
            char data = Serial.read();
            if(data == "P"){
              char data = Serial.read();
              if(data == "G"){
                char data = Serial.read();
                if(data == "L"){
                  for ( int i = 0; i < 300; i++ ) {q
                    Serial.print(Serial.read());
                  }
                  break;
                }
              }
            }
          }
        }
      }
}
