
int SENSOR_PIN = 0; //for analaog
//int SENSOR_PIN = 2;
int Signal;
int treshold;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
   Signal = analogRead(SENSOR_PIN);
  //Signal = digitalRead(SENSOR_PIN);
  Serial.println(Signal);
 
    
  delay(500);
}
