# Intro #

Example code for a simple client-server setup using CircuitPython v8.2.0

Uses the adafruit_rfm9x library which can be found at https://github.com/adafruit/Adafruit_CircuitPython_RFM9x

The adafruit library is an implementation of the RadioHead library (https://www.airspayce.com/mikem/arduino/RadioHead/)

The purpose was to create a simple client and server for testing my RFM95 modules. The server was running on an ESP DEVKIT V1 with CircuitPython installed whilst the client was running on an RPi Pico.

NOTE: The pin settings in the RH_server.py file are for a Pico - you will need to change them.

# Pico Pins

This is how I wired mine on a stripboard

RST=board.GP22
SPI_CS= board.GP17
SPI_MISO= board.GP16
SPI_MOSI=board.GP19
SPI_SCK=board.GP18
LED=board.LED # some boards might not have LED defined

# ESP32 Devkit V1 Pins

This is how I wired mine on a stripboard
RST=board.D4
SPI_CS= board.D5
SPI_MISO= board.D19
SPI_MOSI=board.D23
SPI_SCK=board.D18
LED=board.LED

