# 1.28"-round-tft-to-kb2040.py
# Using a generic 1.28" 240x240 Round TFT LCD
# of type GC9A01A. Wired to a KB2040
import board, displayio, terminalio, busio, time, adafruit_imageload
from adafruit_display_text.bitmap_label import Label
from fourwire import FourWire
from vectorio import Circle
from adafruit_gc9a01a import GC9A01A

# Release any existing displays
displayio.release_displays()

sck = board.D2
mosi = board.D3
spi = busio.SPI(clock=board.D2, MOSI=board.D3)

tft_cs = board.D5  # Chip select
tft_dc = board.D4  # Data/command
tft_reset = board.D6 # Reset

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset)
display = GC9A01A(display_bus, width=240, height=240, rotation=180)

# --- Default Shapes/Text Demo ---
main_group = displayio.Group()
display.root_group = main_group

bg_bitmap = displayio.Bitmap(240, 240, 2)
color_palette = displayio.Palette(2)
color_palette[0] = 0x00FF00  # Bright Green
color_palette[1] = 0xAA0088  # Purple

bg_sprite = displayio.TileGrid(bg_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

inner_circle = Circle(pixel_shader=color_palette, x=120, y=120, radius=100, color_index=1)
main_group.append(inner_circle)

text_group = displayio.Group(scale=2, x=50, y=120)
text = "Hello World!"
text_area = Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
main_group.append(text_group)

# --- ImageLoad Demo ---
blinka_group = displayio.Group()
bitmap, palette = adafruit_imageload.load("/blinka_round.bmp",
                                          bitmap=displayio.Bitmap,
                                          palette=displayio.Palette)

grid = displayio.TileGrid(bitmap, pixel_shader=palette)
blinka_group.append(grid)

print("Code Running!")

while True:
	# show shapes/text
    display.root_group = main_group
    time.sleep(2)
	# show blinka bitmap
    display.root_group = blinka_group
    time.sleep(2)