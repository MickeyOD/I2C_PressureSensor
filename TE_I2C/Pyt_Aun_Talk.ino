// Get pressure sensor data 
// by Songlin Li 2020.07.31
#include<Wire.h>
#define sensor 0x36 //Unique bus address 
char line[2] = ""; // 传入的串行数据
int ret = 0;
unsigned long t0;
unsigned long t1;

void setup() {
  Serial.begin(9600); // 打开串口，设置数据传输速率9600
  Wire.begin();//Wakes up I2C bus 
}

void getdata(byte* e)
{
  //Move register pointer back to first register
  Wire.requestFrom(sensor,2);//Sends content of first two registers
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
  Serial.print(pressure);
  Serial.print("\n");
  //delay(100); // delay 100ms for another loop
}


void loop() {
  t0 = millis();
  // 纯口可用时操作
  if (Serial.available() > 0) {
    // 读取传入的数据: 读到 \n 为止，或者最多500 个字符
    ret = Serial.readBytesUntil("\n", line, 2);
    // Print pressure：
    showdata();
    t1 = millis();
    //Serial.print(t1-t0);
    //Serial.print("ms \n");
    delay(70);
  }
  // 每1ms秒做一个输出
  delay(1);
  //Serial.println("waiting");
}
