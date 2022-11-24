int i = 0;
int PIN = 4;
void setup() {
  // put your setup code here, to run once:
  pinMode(PIN,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(i = 0 ;i<225;i+=50)
   {
    analogWrite(PIN,i);
    delay(500);
   }

}
