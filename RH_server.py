# RH_server
import board
import busio
import digitalio
import time

import adafruit_rfm9x

# wiring pins
RST=board.GP22
SPI_CS= board.GP17
SPI_MISO= board.GP16
SPI_MOSI=board.GP19
SPI_SCK=board.GP18
LED=board.LED # some board might not have LED defined

# Define radio parameters.
RADIO_FREQ_MHZ = 868.1  #

# Define pins connected to the chip, use these if wiring up the breakout according to the guide:
CS = digitalio.DigitalInOut(SPI_CS)
RESET = digitalio.DigitalInOut(RST)


# Define the onboard LED
LED = digitalio.DigitalInOut(LED)
LED.direction = digitalio.Direction.OUTPUT

# Initialize SPI bus.
spi = busio.SPI(SPI_SCK, MOSI=SPI_MOSI, MISO=SPI_MISO)

# Initialze RFM radio
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Note that the radio is configured in LoRa mode so you can't control sync
# word, encryption, frequency deviation, or other settings!

# You can however adjust the transmit power (in dB).  The default is 13 dB but
# high power radios like the RFM95 can go up to 23 dB:
#rfm9x.tx_power = 13

# Send the first packet to get the server to respond.

packet_count=1

def sendPacket():
    global packet_count
    
    rfm9x.send(bytes(f"Server Packet {packet_count}\r\n", "utf-8"))
    print(f"Sent packet {packet_count}")
    packet_count+=1

# Wait to receive packets.  Note that this library can't receive data at a fast

while True:
    packet = rfm9x.receive(timeout=5.0)
    
    # If no packet was received during the timeout then None is returned.
    if packet is None:
        # Packet has not been received
        LED.value = False
        print(".",end="")
    else:
        # Received a packet!
        LED.value = True
        # Print out the raw bytes of the packet:
        print("Received (raw bytes): {0}".format(packet))
        # And decode to ASCII text and print it too.  Note that you always
        # receive raw bytes and need to convert to a text format like ASCII
        # if you intend to do string processing on your data.  Make sure the
        # sending side is sending ASCII data before you try to decode!
        packet_text = str(packet, "ascii")
        print("Received (ASCII): {0}".format(packet_text))
        # Also read the RSSI (signal strength) of the last received message and
        # print it.
        rssi = rfm9x.last_rssi
        print("Received signal strength: {0} dB".format(rssi))
        time.sleep(2)
        sendPacket()

