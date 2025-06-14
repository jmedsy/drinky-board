#include <Wire.h>
#include "ADG2128.h"

ADG2128 chip0(0x70); // A0–A2 = GND
ADG2128 chip1(0x71); // A0 = HIGH, A1/A2 = GND

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        ; // Wait for USB Serial

    Wire.begin();
    Wire.setClock(400000); // Fast mode I2C

    if (!chip0.begin())
    {
        Serial.println("ERR: chip 0x70 not found");
        while (1)
            ;
    }
    if (!chip1.begin())
    {
        Serial.println("ERR: chip 0x71 not found");
        while (1)
            ;
    }

    clearAll();
    Serial.println("Ready for 3-second switch activations.");
}

void loop()
{
    if (Serial.available())
    {
        String input = Serial.readStringUntil('\n');
        input.trim();

        int space = input.indexOf(' ');
        if (space == -1)
            return;

        String p1 = input.substring(0, space);
        String p2 = input.substring(space + 1);

        int c1 = p1.indexOf(',');
        int c2 = p2.indexOf(',');

        if (c1 == -1 || c2 == -1)
            return;

        int r1 = p1.substring(0, c1).toInt();
        int y1 = p1.substring(c1 + 1).toInt();
        int r2 = p2.substring(0, c2).toInt();
        int y2 = p2.substring(c2 + 1).toInt();

        if (!valid(r1, y1) || !valid(r2, y2))
            return;

        chip0.on(r1, y1);
        chip1.on(r2, y2);

        delay(3000); // 3-second hold

        chip0.off(r1, y1);
        chip1.off(r2, y2);

        Serial.print("Held 3s: ");
        Serial.print("X");
        Serial.print(r1);
        Serial.print("↔Y");
        Serial.print(y1);
        Serial.print(" + ");
        Serial.print("X");
        Serial.print(r2);
        Serial.print("↔Y");
        Serial.println(y2);
    }
}

bool valid(int row, int col)
{
    return row >= 0 && row < 12 && col >= 0 && col < 8;
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
