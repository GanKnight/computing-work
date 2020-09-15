from microbit import*
import random
import time
count=10
name =0
while true:
if button.b_is pressed():
  count=count+1
  display.show(count)
  display.scroll('Start spamming A')
  if button_a.was_pressed():
    name=name=1
    display.scroll(name)
if count=0:
  display.scroll("Game over')
    display.show(name)
