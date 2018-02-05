import turtle
from turtle import *
import time
import random
import math
from ball import Ball

running=True

# print(str(getcanvas().winfo_height()))
# print(str(getcanvas().winfo_width()))
# turtle.mainloop()
score=turtle.clone()
#score.ht()
score.pu()
d=50
a=50

hearts=3

health_pos1=(int(680/2) -d,600/2 -d)
health_pos2=(int(680/2) -d-a,600/2 -d)
health_pos3=(int(680/2) -d-a*2,600/2 -d)

health_positions=[(health_pos1),(health_pos2),(health_pos3)]

while running==True:
	for i in range(hearts):
		for position in health_positions:
			score.goto(position)
			score.stamp()

turtle.mainloop()