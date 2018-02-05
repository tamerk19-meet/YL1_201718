from turtle import Turtle
import turtle


class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)	
		self.x= x
		self.y= y
		self.pu()
		self.goto(x,y)
		self.dx= dx
		self.dy= dx
		self.r= r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)

	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x= current_x + self.dx

		current_y=self.ycor()
		new_y= current_y + self.dy	

		right_side_ball= new_x + self.r 
		left_side_ball= new_x - self.r
		top_side_ball= new_y + self.r
		bottom_side_ball= new_y - self.r

		self.goto(new_x,new_y)

		if right_side_ball >= screen_width:
			self.dx= -(self.dx)
			self.clear()

		if left_side_ball <= -screen_width:
			self.dx= -(self.dx)
			self.clear()
	
		if top_side_ball >= screen_height:
			self.dy= -(self.dy)
			self.clear()

		if bottom_side_ball <= -screen_height:	
			self.dy= -(self.dy)
			self.clear()
	def __del__(self):
		print("deleted")

			
			