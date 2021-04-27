void setup() {
  Serial.begin(9600);
  Serial.println("start:");
}

void loop() {
  while(Serial.available()){
    Serial.print(Serial.read());
  }

}
