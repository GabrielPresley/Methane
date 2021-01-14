/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|*   for grad 2021 BSS SRM Class   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

#include <Wire.h>

// address is 0x50
// This is according to the example code in the
// wire library i2c_scanner
#define Addr 0x50
//
void setup()
{
  // open I2C comm. as master
  Wire.begin();
  // set baud rate = 9600
  Serial.begin(9600);
}
//
void loop()
{
  // start I2C
  Wire.beginTransmission(Addr);
//
  // data register/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|*   for grad 2021 BSS SRM Class   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

#include <Wire.h>

// address is 0x50
// This is according to the example code in the
// wire library i2c_scanner
#define Addr 0x50
//
void setup()
{
  // open I2C comm. as master
  Wire.begin();
  // set baud rate = 9600
  Serial.begin(9600);
}
//
void loop()
{
  // start I2C
  Wire.beginTransmission(Addr);
//
  // data register
  Wire.write(0x00);
//
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
// output
  Serial.print("Methane (ppm)");
  Serial.println(ppm);
  delay(1000);
}

  Wire.write(0x00);
//
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
// output
  Serial.print("Methane (ppm)");
  Serial.println(ppm);
  delay(1000);
}
