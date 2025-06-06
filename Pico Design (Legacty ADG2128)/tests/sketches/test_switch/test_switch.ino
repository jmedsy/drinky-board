#include <Wire.h>

#define SWITCH_ADDR 0x71

void setup() {
  Wire.begin();
  delay(100);
  Serial.begin(9600);
  while (!Serial);

  Serial.println("🔒 Closing X7 ↔ Y7 on 0x71");

  Wire.beginTransmission(SWITCH_ADDR);
  Wire.write(0b10000111);  // DATA=1, AX=0111 (X7)
  Wire.write(0b11100001);  // AY=111 (Y7), LDSW=1
  Wire.endTransmission();
}

void loop() {
  // Nothing
}
