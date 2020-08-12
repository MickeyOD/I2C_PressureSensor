#include<Wire.h>
#define sensor 0x5A //Unique bus address 

void setup()
{ 
  Wire.begin();//Wakes up I2C bus 
  Serial.begin(9600);
}

void getdata(byte *a, byte *b, byte *c, byte *d,byte* e)
{
  //Move register pointer back to first register
  //Wire.beginTransmission(sensor);
  //Wire.write(0xB5);
  //Wire.endTransmission();
  Wire.requestFrom(sensor,4);//Sends content of first two registers
  *(e+3) = Wire.read(); //first byte recieved stored here
  *(e+2) = Wire.read(); //second byte recieved stored here
  *(e+1) = Wire.read();
  *(e+0) = Wire.read();
}

void showdata()
{
  long raw;
  byte aa,bb,cc,dd;
  int a = 1;
  long *p = &raw;
  byte *ee = (byte*)p;
 
  
  float pressure =0;
  float temp = 4194304;
  getdata(&aa,&bb,&cc,&dd,ee);
  pressure = (float)raw*1000/(temp)/10;  //kpa

  
  //Serial.print("byte 1: ");Serial.println(aa,DEC);
  //Serial.print("byte 2 ");Serial.println(bb,DEC);
  //Serial.print("byte 3: ");Serial.println(cc,DEC);
  //Serial.print("byte 4 ");Serial.println(dd,DEC);
  Serial.print("Pressure ");
  //Serial.println(raw);
  Serial.print(pressure,4);
  Serial.print('\n');
 delay(100);

}

void loop()
{
  showdata();
}
