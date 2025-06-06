# 1.28-inch-round-tft-circuitpython

Blinka code adapted from demo from Liz Clark at:
https://learn.adafruit.com/adafruit-1-28-240x240-round-tft-lcd/overview

Wiring for the Raspbery Pi Pico Series Boards:

Display 	->	Pico Pin
- VCC	Power ->	3.3V	🔴 Red
- GND	Ground ->	GND	⚫ Black
- SCL	SPI Clock ->	GP18	🟡 Yellow
- SDA	SPI MOSI ->	GP19	🔵 Blue	MOSI (data from microcontroller)
- DC	Data/Command ->	GP21	🟢 Green
- TCS	Chip Select ->	GP20	⚪.  White,	Selects the display on SPI bus
- RST	Reset	-> GP15	🟣 Purple

<img width="800" alt="wiring diagram" src="https://github.com/user-attachments/assets/4485f470-5ce0-41c5-9468-647d5afeb9ed" />

[![Watch the video](https://img.youtube.com/vi/zZ6A1ND1vQ0/maxresdefault.jpg)](https://youtu.be/zZ6A1ND1vQ0)

I wired this on a KB2040 for our "Display of Displays" at school using this scheme:

Display 	->	KB2040 Pin
- VCC	Power ->	3V	🔴 Red
- GND	Ground ->	GND	⚫ Black
- SCL	SPI Clock ->	GP2	🟡 Yellow
- SDA	SPI MOSI ->	GP3	🟢 Green	MOSI (data from microcontroller)
- DC	Data/Command ->	GP4	🔵 Blue
- CS	Chip Select ->	GP5	🟣 Purple,	Selects the display on SPI bus
- RST	Reset	-> GP6	🟠 Orange


