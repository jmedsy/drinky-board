// Using https://github.com/RobTillaart/ADG2128_RT

// Used to test the ADG2128 chip.
// Example command: 0,0 2,3
// This will activate the switch at row 0, column 0 on chip 0 and the switch at row 2, column 3 on chip 1

#include <Wire.h>
#include "ADG2128.h"

ADG2128 chip0(0x70); // ADG2128 with A0–A2 = GND
ADG2128 chip1(0x71); // ADG2128 with A0 = HIGH, A1/A2 = GND

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        ; // Wait for USB Serial

    Serial.println("ADG2128 Dual-Chip Command Mode");
    ß
        Serial.println("Send: row1,col1 row2,col2  (e.g., 0,0 2,3)");

    Wire.begin();
    Wire.setClock(400000);

    if (!chip0.begin())
    {
        Serial.println("Error connecting to chip @ 0x70");
        while (1)
            ;
    }

    if (!chip1.begin())
    {
        Serial.println("Error connecting to chip @ 0x71");
        while (1)
            ;
    }

    clearAll();
    Serial.println("All switches cleared.");
}

void loop()
{
    if (Serial.available())
    {
        String input = Serial.readStringUntil('\n');
        input.trim();

        int spaceIndex = input.indexOf(' ');
        if (spaceIndex == -1)
        {
            Serial.println("ERR: Expected format row1,col1 row2,col2");
            return;
        }

        String pair1 = input.substring(0, spaceIndex);
        String pair2 = input.substring(spaceIndex + 1);

        int comma1 = pair1.indexOf(',');
        int comma2 = pair2.indexOf(',');

        if (comma1 == -1 || comma2 == -1)
        {
            Serial.println("ERR: Invalid format in one of the pairs");
            return;
        }

        int row1 = pair1.substring(0, comma1).toInt();
        int col1 = pair1.substring(comma1 + 1).toInt();
        int row2 = pair2.substring(0, comma2).toInt();
        int col2 = pair2.substring(comma2 + 1).toInt();

        if (!validIndex(row1, col1) || !validIndex(row2, col2))
        {
            Serial.println("ERR: Index out of range (row 0–11, col 0–7)");
            return;
        }

        clearAll();

        chip0.on(row1, col1);
        chip1.on(row2, col2);

        Serial.print("Activated X");
        Serial.print(row1);
        Serial.print("↔Y");
        Serial.print(col1);
        Serial.print(" on 0x70, X");
        Serial.print(row2);
        Serial.print("↔Y");
        Serial.print(col2);
        Serial.println(" on 0x71");
    }
}

bool validIndex(int row, int col)
{
    return (row >= 0 && row < 12) && (col >= 0 && col < 8);
}

void clearAll()
{
    for (int r = 0; r < 12; r++)
    {
        for (int c = 0; c < 8; c++)
        {
            chip0.off(r, c);
            chip1.off(r, c);
        }
    }
}
