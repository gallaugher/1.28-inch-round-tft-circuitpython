# 1.28-inch-round-tft-circuitpython

Blinka code adapted from demo from Liz Clark at:
https://learn.adafruit.com/adafruit-1-28-240x240-round-tft-lcd/overview


I wired this on a KB2040 for our "Display of Displays" at school using this scheme:

Display 	->	KB2040 Pin
VCC	Power ->	3V	🔴 Red
GND	Ground ->	GND	⚫ Black
SCL	SPI Clock ->	GP2	🟡 Yellow
SDA	SPI MOSI ->	GP3	🟢 Green	MOSI (data from microcontroller)
DC	Data/Command ->	GP4	🔵 Blue	
CS	Chip Select ->	GP5	🟣 Purple,	Selects the display on SPI bus
RST	Reset	-> GP6	🟠 Orange
