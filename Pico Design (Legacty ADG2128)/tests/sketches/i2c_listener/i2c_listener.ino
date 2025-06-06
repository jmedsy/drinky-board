#include <Wire.h>

#define SWITCH1_ADDR 0x71
#define SWITCH2_ADDR 0x70

void setup() {
  Wire.begin();
  Serial.begin(9600);
  while (!Serial);
  Serial.println("🟢 ItsyBitsy I2C listener ready");
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "PRESS A") {
      pressCombo();
    }
  }
}

void writeSwitch(uint8_t addr, uint8_t x, uint8_t y, bool connect) {
  Wire.beginTransmission(addr);
  Wire.write(0x80 | (x & 0x0F));  // Control register for Xn
  Wire.write(1 << y);             // Bitmask for Yn
  Wire.endTransmission();
}

void pressCombo() {
  // Open both switches
  writeSwitch(SWITCH1_ADDR, 7, 7, true);  // X7 ↔ Y7
  writeSwitch(SWITCH2_ADDR, 0, 7, true);  // X0 ↔ Y7

  delay(40);  // Simulate keypress duration

  // Close both switches
  writeSwitch(SWITCH1_ADDR, 7, 7, false);
  writeSwitch(SWITCH2_ADDR, 0, 7, false);
}
