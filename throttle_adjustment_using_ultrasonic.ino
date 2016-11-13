#include <Servo.h>
#define trigPin 13
#define echoPin 12

Servo Throttle;

int pin_in = 7;
int pin_out = 6;


unsigned long rc_throttle;



void setup()

{
  
  Throttle.attach(pin_out);
  pinMode(pin_in,INPUT);
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}



void loop()

{

/*
 CODE FOR RECEIVING RC_THROTTLE
 
  rc_throttle = pulseIn(pin_in, HIGH);

  Serial.print("old - ");
  Serial.println(rc_throttle);  

*/

 long duration, distance;
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2); // Added this line
  digitalWrite(trigPin, HIGH);
//  delayMicroseconds(1000); - Removed this line
  delayMicroseconds(10); // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1; 


  if (distance >= 200 || distance <= 0){
    Serial.print("Out of range but distance is: ");
    Serial.println(distance);
    rc_throttle = 0;
  }
  
  if (distance >=1 && distance <=50){
    Serial.print(distance);
    Serial.println(" cm");
    rc_throttle = 1900;
  }
  if (distance >= 51 && distance <=100){
    Serial.print(distance);
    Serial.println(" cm");
    rc_throttle = 1700;
  }
  if (distance >= 101 && distance <=150){
    Serial.print(distance);
    Serial.println(" cm");
    rc_throttle = 1500;
  }

  if (distance >=151 && distance <=199){
    Serial.print(distance);
    Serial.println(" cm");
    rc_throttle = 1200;
  }




  delay(250);

  
  Throttle.writeMicroseconds(rc_throttle);

  Serial.print("throttle value- ");
  Serial.println(rc_throttle);


  }


