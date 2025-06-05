# 1.28"-round-tft-to-kb2040.py
# Using a generic 1.28" 240x240 Round TFT LCD
# of type GC9A01A. Wired to a KB2040
import board, displayio, terminalio, busio, time, adafruit_imageload, math, random
from adafruit_display_text.bitmap_label import Label
from fourwire import FourWire
from vectorio import Circle
from adafruit_gc9a01a import GC9A01A

# Release any existing displays
displayio.release_displays()

# wiring for QT Py, should work on any QT Py or XIAO board
tft0_clk  = board.D2
tft0_mosi = board.D3
tft_L0_dc  = board.D4
tft_L0_cs  = board.D5
tft_L0_rst = board.D6

spi0 = busio.SPI(clock=tft0_clk, MOSI=tft0_mosi)
#
# sck = board.D2
# mosi = board.D3
# spi = busio.SPI(clock=board.D2, MOSI=board.D3)
#
# tft_cs = board.D5  # Chip select
# tft_dc = board.D4  # Data/command
# tft_reset = board.D6 # Reset
#
# display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset)
# display = GC9A01A(display_bus, width=240, height=240, rotation=180)
#
# displayio.release_displays()

dw, dh = 240,240  # display dimensions

# load our eye and iris bitmaps
eyeball_bitmap, eyeball_pal = adafruit_imageload.load("imgs/eye0_ball2.bmp")
iris_bitmap, iris_pal = adafruit_imageload.load("imgs/eye0_iris0.bmp")
iris_pal.make_transparent(0)  # palette color #0 is our transparent background

# compute or declare some useful info about the eyes
iris_w, iris_h = iris_bitmap.width, iris_bitmap.height  # iris is normally 110x110
iris_cx, iris_cy = dw//2 - iris_w//2, dh//2 - iris_h//2
r = 20  # allowable deviation from center for iris

# class to help us track eye info (not needed for this use exactly, but I find it interesting)
class Eye:
    def __init__(self, spi, dc, cs, rst, rot=0, eye_speed=0.25, twitch=2):
        display_bus = displayio.FourWire(spi, command=dc, chip_select=cs, reset=rst)
        display = GC9A01A(display_bus, width=dw, height=dh, rotation=rot)
        main = displayio.Group()
        display.root_group = main
        self.display = display
        self.eyeball = displayio.TileGrid(eyeball_bitmap, pixel_shader=eyeball_pal)
        self.iris = displayio.TileGrid(iris_bitmap, pixel_shader=iris_pal, x=iris_cx,y=iris_cy)
        main.append(self.eyeball)
        main.append(self.iris)
        self.x, self.y = iris_cx, iris_cy
        self.tx, self.ty = self.x, self.y
        self.next_time = time.monotonic()
        self.eye_speed = eye_speed
        self.twitch = twitch

    def update(self):
        self.x = self.x * (1-self.eye_speed) + self.tx * self.eye_speed # "easing"
        self.y = self.y * (1-self.eye_speed) + self.ty * self.eye_speed
        self.iris.x = int( self.x )
        self.iris.y = int( self.y )
        if time.monotonic() > self.next_time:
            t = random.uniform(0.25,self.twitch)
            self.next_time = time.monotonic() + t
            self.tx = iris_cx + random.uniform(-r,r)
            self.ty = iris_cy + random.uniform(-r,r)
        self.display.refresh()

# a list of all the eyes, in this case, only one
the_eyes = [
    Eye( spi0, tft_L0_dc, tft_L0_cs,  tft_L0_rst, rot=0),
]

while True:
    for eye in the_eyes:
        eye.update()
