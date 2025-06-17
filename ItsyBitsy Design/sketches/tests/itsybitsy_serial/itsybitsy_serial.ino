#include <Arduino.h>

// ItsyBitsy 32u4 Serial Command Handler
// This sketch listens for serial commands to control pins

void setup()
{
    Serial.begin(9600); // Start serial at 9600 baud
    while (!Serial)
    {
        ; // Wait for serial port to connect
    }

    // Initialize pins here
    // Add your pin configurations as needed
}

void loop()
{
    if (Serial.available() > 0)
    {
        String command = Serial.readStringUntil('\n');
        command.trim(); // Remove any whitespace

        // Parse and handle the command
        // Example command format: "PIN,STATE" (e.g., "13,HIGH")
        int commaIndex = command.indexOf(',');
        if (commaIndex != -1)
        {
            int pin = command.substring(0, commaIndex).toInt();
            String state = command.substring(commaIndex + 1);

            if (state == "HIGH")
            {
                digitalWrite(pin, HIGH);
                Serial.println("OK: " + command);
            }
            else if (state == "LOW")
            {
                digitalWrite(pin, LOW);
                Serial.println("OK: " + command);
            }
            else
            {
                Serial.println("ERR: Invalid state");
            }
        }
        else
        {
            Serial.println("ERR: Invalid command format");
        }
    }
}