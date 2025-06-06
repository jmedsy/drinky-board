#include <Wire.h>

void setup() {
  Wire.begin();
  Serial.begin(9600);
  while (!Serial);

  delay(500);
  Serial.println("🔍 I2C Scanner running...");

  for (byte addr = 0x03; addr <= 0x77; addr++) {
    Wire.beginTransmission(addr);
    if (Wire.endTransmission() == 0) {
      Serial.print("✅ Found device at 0x");
      Serial.println(addr, HEX);
    }
  }
}

void loop() {
}
