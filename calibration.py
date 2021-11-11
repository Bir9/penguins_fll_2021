#!/usr/bin/env pybricks-micropython
import time 
from robot import Robot

from pybricks.parameters import Button
from pybricks.media.ev3dev import Font

#def calibration(ev3, left_cs, right_cs, right_wheel, left_wheel, ultra_sonic, gyro): #add any extra sensor/motors, I can not as I would get an error

if __name__ == "__main__":
  r = Robot()

  button_pressed = False
  r.ev3.screen.set_font(Font(family=None, size=12, bold=True))
  while button_pressed == False:
      left_cs_string = "Left CS:", str(r.left_cs.reflection())
      right_cs_string = "Right CS:", str(r.right_cs.reflection())
      left_wheel_string = "Left Wheel:", str(r.left_wheel.angle())
      right_wheel_string = "Right Wheel:", str(r.right_wheel.angle())
      ultra_sonic_string = "US:", str(r.ultra_sonic.distance(False))
      gyro_string = "Gyro:", str(r.gyro.angle())
      curr_value_string = "CV", str(r.cs_threshold)
      r.ev3.screen.draw_text(0, 0, left_cs_string)
      r.ev3.screen.draw_text(0, 30, right_cs_string)
      r.ev3.screen.draw_text(0, 60, left_wheel_string)
      r.ev3.screen.draw_text(0, 90, right_wheel_string)
      r.ev3.screen.draw_text(85, 0, ultra_sonic_string)
      r.ev3.screen.draw_text(100, 30, gyro_string)
      r.ev3.screen.draw_text(100, 30, curr_value_string)
      time.sleep(0.2)
      r.ev3.screen.clear()
      if(r.ev3.buttons.pressed() == [Button.CENTER]):
          button_pressed = True
      else:
          button_pressed = False
  str_value = str(r.left_cs.reflection())
  file_handler = open("Calibration.txt", "w")
  file_handler.write(str_value)
  file_handler.close()
        
