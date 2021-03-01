#include <SoftwareSerial.h>
int PulseSensorPurplePin = 0;       
int LED13 = 13;  
int Signal;                
int Threshold = 550;            
int S;
SoftwareSerial mySerial(10, 11); // RX, TX
void setup() 
{
   pinMode(LED13,OUTPUT);         // pin that will blink to your heartbeat!
   Serial.begin(9600);         // Set's up Serial Communication at certain speed.
   mySerial.begin(9600);
}
void loop() 
{

  Signal = analogRead(PulseSensorPurplePin);
  S=(Signal/8);                                            
  Serial.print("Your heart Beat is : ");
  Serial.println(S);
  mySerial.println(S);
  if(Signal > Threshold)
    {                          
     digitalWrite(LED13,HIGH);
    } 
    else 
    {
     digitalWrite(LED13,LOW);               
    }
delay(1000);
}