
long dis1,dis2,dis3;
long dur1,dur2,dur3;

int echo1=2, echo2=3, echo3=4;
int trig1=8, trig2=9, trig3=7;


void setup() 
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  // put your setup code here, to run once:
  pinMode(echo1, INPUT);
  pinMode(echo2, INPUT);
  pinMode(echo3, INPUT);


  pinMode(trig1, OUTPUT);
  pinMode(trig2, OUTPUT);
  pinMode(trig3, OUTPUT);

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
  dur1 = pulseIn(echo1, HIGH);

  // Calculating the distance
  dis1 = dur1 * 0.034 / 2;

  if(dis1<10 && dis1>=0) {
    digitalWrite(13, HIGH);
  }
  else digitalWrite(13, LOW);

  digitalWrite(trig2, LOW);
  delayMicroseconds(2);

  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trig2, 0x01);
  delayMicroseconds(10);
  digitalWrite(trig2, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  dur2 = pulseIn(echo2, HIGH);

  // Calculating the distance
  dis2 = dur2 * 0.034 / 2;

  if(dis2<10 && dis2>=0) {
    digitalWrite(12, HIGH);
  }
  else digitalWrite(12, LOW);

  digitalWrite(trig3, LOW);
  delayMicroseconds(2);

  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trig3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig3, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  dur3 = pulseIn(echo3, HIGH);

  // Calculating the distance
  dis3 = dur3 * 0.034 / 2;

  if(dis3<100 && dis3>=0) {
    digitalWrite(11, HIGH);
  }
  else digitalWrite(11, LOW);
}
