/*
HC-SR04 Ultrasonic Sensor
Arduino UNO
*/
long distance;
long duration;

int echo1=2;
int trig1=8;

void setup() 
{
  pinMode(13, OUTPUT);
  // put your setup code here, to run once:
  pinMode(echo1, INPUT);


  pinMode(trig1, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  

  // Clears the trigPin condition
  digitalWrite(trig1, LOW);
  delayMicroseconds(2);

  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trig1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig1, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echo1, HIGH);

  // Calculating the distance
  distance = duration * 0.034 / 2;

  if(distance<10 && distance>=0) {
    digitalWrite(13, HIGH);
  }
  else digitalWrite(13, LOW);
}
