from turtle import *
from random import randint, choice

#### CLASS AND FUNCTION DEFINITIONS #####
def playing_area():
	t = Turtle()
	t.speed(0)
	t.ht()
	t.pu()
	t.goto(-250,250)
	t.color("light blue")
	t.pd()
	t.begin_fill()
	for i in range(4):
		t.forward(500)
		t.right(90)
	t.end_fill()

'''
Player() Class

Constructor( def __init__(self)):
- player should be shaped like a turtle.
- will take in the x and y coordinates for where the player will initially appear.
- will take in a color for the player
- will take in keys to turn left, turn right and shoot bullets.
- player will have an attribute that is a list that stores bullets




fire(self):
- creates a Bullet object
- appends the Bullet object to the players's bullet list
'''
class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.player_color = color
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def fire(self):
        self.bullets.append(Bullet(self))

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(5)
        if self.xcor() > 250 or self.xcor() < -250:
            self.setheading(180 - self.heading())
        if self.ycor() > 250 or self.ycor() < -250:
            self.setheading(-self.heading())

    def kill_turtle(self):
        if self.health <= 0:
            self.clear()
            self.ht()
            self.alive = False

        if self.health ==2:
            self.pencolor("Yellow")
        elif self.health ==1:
            self.pencolor("Red")



class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(player.player_color)
        self.pu()
        self.goto(player.xcor(), player.ycor())
        self.setheading(player.heading())
        self.player = player
        self.st()

    def die(self):
        if self in self.player.bullets:
            self.ht()
            self.player.bullets.remove(self)
    

    def move(self):
        self.forward(15)
        if self.xcor() > 250 or self.xcor() < -250:
            self.die()
        if self.ycor() > 250 or self.ycor() < -250:
            self.die()


class Prize(Turtle):
	def __init__(self):
		super().__init__()
		self.speed(1)
		self.shape("circle")
		self.color("yellow")
		self.penup()
		self.goto(randint(-250, 250), randint(-250, 250))
		self.setheading(randint(0,360))
          

	def relocate(self):
		self.goto(randint(-250, 250), randint(-250, 250))
		self.setheading(randint(0,360))

	def move(self):
		self.forward(2)
		if self.xcor() > 250 or self.xcor() < -250:
			self.setheading(180 - self.heading())
		if self.ycor() > 250 or self.ycor() < -250:
			self.setheading(-self.heading())

     




class Zombie(Turtle):
	def __init__(self):
		super().__init__()
		self.speed(1)
		self.shape("turtle")
		self.color("green")
		self.penup()
    

	def move(self):
		zombie.setheading(zombie.towards(p1))
		zombie.forward(2)
      
	


	def die(self):
		self.clear()
		self.ht()
		self.alive = False


class Bomb(Turtle):
	def __init__(self):
		super().__init__()
		self.bombs = []
		self.speed(0)
		self.hideturtle()
		self.color("red")
		self.penup()
		self.goto(player.xcor(), player.ycor())
            
	
#Bomb Class:
# Will originate at the location of the Player object that dropped it.

# Each Bomb object will:

# Be placed at the player’s current position
# Wait for a short delay (~1 second) before exploding
# When the bomb explodes:

# A circular blast radius of approximately 100 pixels will be drawn
# All Zombie objects within this radius will be destroyed and removed from the game
# After exploding:

# The bomb will remove itself from the player’s bomb list
# The explosion drawing will be cleared

	def explode(self):
		pass




def update():
	while p1.alive and p2.alive:
		p1.move()
		p2.move()
		for bullet in p1.bullets:
			bullet.move()
		for bullet in p2.bullets:
			bullet.move()
		prize.move()

		if p1.distance(prize) < 20 or p2.distance(prize) <20:
			prize.relocate()


#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")
screen.listen()

p1 = Player(-100, 0, "blue", screen, "d", "a", "w")
p2 = Player(100,0,"red",screen, "Right","Left", 'Up')
prize = Prize()


playing_area()

screen.ontimer(update(), 50)

screen.mainloop()
