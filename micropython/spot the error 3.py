from microbit import*
count = 0 #added variable
while True:
  if button_a.was_pressed(): #changed to button a instead
    display.show(Image.RABBIT) #Capatilized the 'i'
    count = count+1
  if count == 0: #Made it equivalent to zero for function to perform
    display.show(Image.TORTOISE)
  if button_b.was_pressed():
    display.show(Image.SNAKE) #Hare doesnt exist
 
#There are multiple errors
#You can choose to fix one question max.
