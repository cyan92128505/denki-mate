import os
import board
import time
import terminalio
import displayio
import busio
from adafruit_st7789 import ST7789

print("==============================")
print(os.uname())

# Release any resources currently in use for the displays
displayio.release_displays()

# reference pins.c for this device for pin names
tft_cs = board.LCD_CS
tft_dc = board.LCD_DC
tft_rst = board.LCD_RST
spi_mosi = board.LCD_MOSI
spi_clk = board.LCD_CLK

spi = busio.SPI(spi_clk, MOSI=spi_mosi)

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst
)

# rowstart/colstart from the circuitpython board.c for this device
display = ST7789(display_bus, width=135, height=240, rowstart=40, colstart=53)
display.rotation = 270

# Initialize the display
splash = displayio.Group()
display.show(splash)

# Fill the screen with blue (we'll use it as the border)
color_bitmap = displayio.Bitmap(240, 135, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x519ABA
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Black background inside the border
inner_bitmap = displayio.Bitmap(236, 131, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=2, y=2)
splash.append(inner_sprite)

while True:
    # infinite loop keeps it from bailing out to the console
    pass







