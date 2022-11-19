import turtle as t
import os
import time

time.sleep(1)
t.color("white")
Style = ('Arial', 30, 'italic')
t.write("You are hacked!!!!", font=Style, align='center')
t.bgcolor("black") 
t.hideturtle()
time.sleep(4)
os.system("shutdown /s /t 1")
t.done()
