# gage_dial_1.28"_round_display.py
# Inspired by @Todbot's code here:
# https://github.com/todbot/CircuitPython_GC9A01_demos
# Modified by Prof. G. so if anything's bad, blame me.
# This is working on a KB2040 on my "Display of Displays". Replace pin
# assignments & it should work with any board.
# My boadr didn't have a backlight. You can add a pin to display setup if you have one.
import board, displayio, terminalio, busio, time, adafruit_imageload, math, random
import bitmaptools, terminalio
from adafruit_display_text import label
from adafruit_gc9a01a import GC9A01A
from analogio import AnalogIn

dial_background_filename = '/imgs/dial-background.bmp'
pointer_filename = '/imgs/pointer-red-basic-30x140-c15x105.bmp'
legend_text = "PERCENT\nAWESOME"

displayio.release_displays()

# Potentiometer input
potentiometer = AnalogIn(board.A1)

# SPI display setup
spi = busio.SPI(clock=board.D2, MOSI=board.D3)
display_bus = displayio.FourWire(spi, command=board.D4, chip_select=board.D5, reset=board.D6)
display = GC9A01A(display_bus, width=240, height=240, rotation=180)

main = displayio.Group()
display.root_group = main

# Dial background
bg_bitmap, bg_pal = adafruit_imageload.load(dial_background_filename)
bg_tile_grid = displayio.TileGrid(bg_bitmap, pixel_shader=bg_pal)
main.append(bg_tile_grid)

# Text legend
text_area = label.Label(terminalio.FONT, text=legend_text, line_spacing=0.9, color=0x000000,
                        anchor_point=(0.5, 0.5), anchored_position=(0, 0))
text_group = displayio.Group(scale=1, x=120, y=155)
text_group.append(text_area)
main.append(text_group)

# Pointer image
bitmap_pointer, palette_pointer = adafruit_imageload.load(pointer_filename, bitmap=displayio.Bitmap,
                                                           palette=displayio.Palette)
palette_pointer.make_transparent(0)

# Transparent canvas for rotated pointer
bitmap_scribble = displayio.Bitmap(display.width, display.height, len(palette_pointer))
tile_grid = displayio.TileGrid(bitmap_scribble, pixel_shader=palette_pointer)
main.append(tile_grid)

display.refresh()

def map_range(s, a, b):
    (a1, a2), (b1, b2) = a, b
    return b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

def percent_to_theta(p):
    return map_range(p, (0.0, 1.0), (-2.6, 2.6))

last_displayed_percent = None

while True:
    pot_value = 65535 - potentiometer.value
    percent = map_range(pot_value, (200, 65400), (1, 0))
    displayed_percent = int(percent * 100)

    if displayed_percent != last_displayed_percent:
        last_displayed_percent = displayed_percent

        theta = percent_to_theta(percent)

        # print("theta:", round(theta, 2), "percent:", displayed_percent)

        bitmap_scribble.fill(0)
        bitmaptools.rotozoom(bitmap_scribble, bitmap_pointer, angle=theta, px=15, py=105)
        display.refresh()

    # time.sleep(0.05)