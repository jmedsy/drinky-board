#include <Wire.h>
#include "ADG2128.h"

enum Axis
{
    X = 0,
    Y = 1
};

enum Action
{
    RELEASE = 0,
    PRESS = 1
};

ADG2128 chip0(0x70);
ADG2128 chip1(0x71);

// Command structure to match Python's KEY object
struct KeyCommand
{
    uint8_t row_i2c_addr;        // I2C address
    uint8_t row_logi_pin;        // Logitech pin
    uint8_t row_pin_axis;        // 0 or 1, respectively X or Y from ADG2128 datasheet
    uint8_t row_pin_channel;     // ADG2128 pin channel (0-11 for X, 0-7 for Y)
    uint8_t row_bus_pin_axis;    // Bus pin axis
    uint8_t row_bus_pin_channel; // Bus pin channel
    uint8_t col_i2c_addr;
    uint8_t col_logi_pin;
    uint8_t col_pin_axis;
    uint8_t col_pin_channel;
    uint8_t col_bus_pin_axis;
    uint8_t col_bus_pin_channel;
    uint8_t action;
};

// Structure for explicitly mapping a key to a command
struct KeyMapping
{
    uint8_t row_pin_axis;
    uint8_t row_pin_channel;
    uint8_t col_pin_axis;
    uint8_t col_pin_channel;
    int itsybitsy_pin;
};

KeyMapping left_shift_key = {0, 10, 1, 2, 0};
KeyMapping left_alt_key = {1, 5, 0, 8, 18};
KeyMapping left_ctrl_key = {0, 11, 0, 0, 19};
KeyMapping left_windows_key = {1, 6, 1, 4, 20};

void setup()
{
    Serial.begin(115200);
    Wire.begin();
    Wire.setClock(400000); // Fast mode I2C

    // Wait for serial connection
    while (!Serial)
    {
        delay(10);
    }

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
    // Check for incoming command
    if (Serial.available() >= sizeof(KeyCommand))
    {
        KeyCommand cmd;
        Serial.readBytes((char *)&cmd, sizeof(KeyCommand));

        // delay(5); // Add delay if having problems

        // Process the command
        performAction(cmd.action, cmd.row_pin_axis, cmd.row_pin_channel, cmd.row_bus_pin_axis, cmd.row_bus_pin_channel,
                      cmd.col_pin_axis, cmd.col_pin_channel, cmd.col_bus_pin_axis, cmd.col_bus_pin_channel);
    }
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
    digitalWrite(left_shift_key.itsybitsy_pin, LOW);
    digitalWrite(left_ctrl_key.itsybitsy_pin, LOW);
    digitalWrite(left_alt_key.itsybitsy_pin, LOW);
    digitalWrite(left_windows_key.itsybitsy_pin, LOW);
}

void performAction(uint8_t action, uint8_t row_pin_axis, uint8_t row_pin_channel, uint8_t row_bus_axis, uint8_t row_bus_channel, uint8_t col_pin_axis, uint8_t col_pin_channel, uint8_t col_bus_axis, uint8_t col_bus_channel)
{
    /* Modifier Key(s) */
    // Left Shift
    if (
        row_pin_axis == left_shift_key.row_pin_axis &&
        row_pin_channel == left_shift_key.row_pin_channel &&
        col_pin_axis == left_shift_key.col_pin_axis &&
        col_pin_channel == left_shift_key.col_pin_channel)
    {
        switch (action)
        {
        case RELEASE:
            pinMode(left_shift_key.itsybitsy_pin, OUTPUT);
            digitalWrite(left_shift_key.itsybitsy_pin, LOW);
            break;
        case PRESS:
            pinMode(left_shift_key.itsybitsy_pin, OUTPUT);
            digitalWrite(left_shift_key.itsybitsy_pin, HIGH);
            break;
        }
    }
    // Left Ctrl
    else if (
        row_pin_axis == left_ctrl_key.row_pin_axis &&
        row_pin_channel == left_ctrl_key.row_pin_channel &&
        col_pin_axis == left_ctrl_key.col_pin_axis &&
        col_pin_channel == left_ctrl_key.col_pin_channel)
    {
        switch (action)
        {
        case RELEASE:
            pinMode(left_ctrl_key.itsybitsy_pin, OUTPUT);
            digitalWrite(left_ctrl_key.itsybitsy_pin, LOW);
            break;
        case PRESS:
            pinMode(left_ctrl_key.itsybitsy_pin, OUTPUT);
            digitalWrite(left_ctrl_key.itsybitsy_pin, HIGH);
            break;
        }
    }
    // Left Alt
    else if (
        row_pin_axis == left_alt_key.row_pin_axis &&
        row_pin_channel == left_alt_key.row_pin_channel &&
        col_pin_axis == left_alt_key.col_pin_axis &&
        col_pin_channel == left_alt_key.col_pin_channel)
    {
        switch (action)
        {
        case RELEASE:
            pinMode(left_alt_key.itsybitsy_pin, OUTPUT);
            digitalWrite(left_alt_key.itsybitsy_pin, LOW);
            break;
        case PRESS:
            pinMode(left_alt_key.itsybitsy_pin, OUTPUT);
            digitalWrite(left_alt_key.itsybitsy_pin, HIGH);
            break;
        }
    }
    // Left Windows
    else if (
        row_pin_axis == left_windows_key.row_pin_axis &&
        row_pin_channel == left_windows_key.row_pin_channel &&
        col_pin_axis == left_windows_key.col_pin_axis &&
        col_pin_channel == left_windows_key.col_pin_channel)
    {
        switch (action)
        {
        case RELEASE:
            pinMode(left_windows_key.itsybitsy_pin, OUTPUT);
            digitalWrite(left_windows_key.itsybitsy_pin, LOW);
            break;
        case PRESS:
            pinMode(left_windows_key.itsybitsy_pin, OUTPUT);
            digitalWrite(left_windows_key.itsybitsy_pin, HIGH);
            break;
        }
    }
    /* All other keys */
    else
    {
        switch (action)
        {
        case RELEASE:
            switch (row_pin_axis)
            {
            case X:
                chip0.off(row_pin_channel, row_bus_channel);
                break;
            case Y:
                chip0.off(row_bus_channel, row_pin_channel);
                break;
            }
            switch (col_pin_axis)
            {
            case X:
                chip1.off(col_pin_channel, col_bus_channel);
                break;
            case Y:
                chip1.off(col_bus_channel, col_pin_channel);
                break;
            }
            break;
        case PRESS:
            switch (row_pin_axis)
            {
            case X:
                chip0.on(row_pin_channel, row_bus_channel);
                break;
            case Y:
                chip0.on(row_bus_channel, row_pin_channel);
                break;
            }
            switch (col_pin_axis)
            {
            case X:
                chip1.on(col_pin_channel, col_bus_channel);
                break;
            case Y:
                chip1.on(col_bus_channel, col_pin_channel);
                break;
            }
            break;
        }
    }
}