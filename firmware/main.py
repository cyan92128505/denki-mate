import os, sys, io
import M5
from M5 import *
from hardware import *


panel = None
textAxis = None
text = None


Count = None

# 描述该功能...
def showAxis():
  global Count, panel, textAxis, text
  textAxis.setText(str(Imu.getAccel()))
  textAxis.setVisible(True)

# Describe this function...
def showText():
  global Count, panel, textAxis, text
  text.setCursor(x=0, y=0)
  text.setText(str(Count))
  text.setVisible(True)
  text.setColor(0xffffff, 0x519aba)

# 描述该功能...
def showRect():
  global Count, panel, textAxis, text
  panel.setCursor(x=20, y=20)
  panel.setSize(w=50, h=50)
  panel.setColor(color=0x33cc00, fill_c=0x33cc00)
  panel.setVisible(True)


def btnA_wasClicked_event(state):
  global panel, textAxis, text, Count
  Count = Count + 1
  showText()


def btnB_wasClicked_event(state):
  global panel, textAxis, text, Count
  Count = Count - 1
  showText()


def setup():
  global panel, textAxis, text, Count

  M5.begin()
  panel = Widgets.Rectangle(0, 0, 1, 1, 0xffffff, 0xffffff)
  textAxis = Widgets.Label("Text", 0, 50, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  text = Widgets.Label("Text", 0, 0, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)

  BtnA.setCallback(type=BtnA.CB_TYPE.WAS_CLICKED, cb=btnA_wasClicked_event)
  BtnB.setCallback(type=BtnB.CB_TYPE.WAS_CLICKED, cb=btnB_wasClicked_event)

  Widgets.fillScreen(0x519aba)
  Widgets.setRotation(3)
  Count = 0
  showText()
  showRect()


def loop():
  global panel, textAxis, text, Count
  M5.update()


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
