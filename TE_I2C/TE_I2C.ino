// Get pressure sensor data 
// by Songlin Li 2020.07.31
#include<Wire.h>
#define sensor 0x36 //Unique bus address 

void setup()
{ 
  Wire.begin();//Wakes up I2C bus 
  Serial.begin(9600);
}

void getdata(byte* e)
{
  //Move register pointer back to first register
  Wire.requestFrom(sensor,2);//Sends content of first two registers
  //*(e+3) = Wire.read(); first byte recieved stored here
  //*(e+2) = Wire.read(); second byte recieved stored here
  *(e+1) = Wire.read(); //first byte(upper 6bits) recieved stored here
  *(e+0) = Wire.read(); //second byte(lower 8bits) recieved stored here
}

void showdata()
{
  int raw;
  int *p = &raw;
  byte *ee = (byte*)p;
  float pressure =0;
  getdata(ee);
  pressure = (float(raw)-819.15)/491.49*6.8947; // kpa output
  // show data
  Serial.print("Pressure ");
  Serial.print(pressure);
  Serial.print("kpa \n");
  delay(100); // delay 100ms for another loop
}

void loop()
{
  showdata();
}
