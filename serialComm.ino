#include <Servo.h>
char dataString[50] = {0}; 

unsigned long rc_ch7;
int ch7_in = 7; 

void setup() {
  pinMode(ch7_in, INPUT);
  Serial.begin(9600);              //Starting serial communication
}
  
void loop() {
  rc_ch7 = pulseIn(ch7_in, HIGH);
  //Serial.println(rc_ch7); 
  if (rc_ch7 > 800 && rc_ch7 < 2200){
    sprintf(dataString,"%02X",rc_ch7); // convert a value to hexa 
    Serial.println(dataString);   // send the data
    delay(100);                    // give the loop some break
  }
}
