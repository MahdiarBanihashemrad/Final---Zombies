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


	def spawn_zombies(self, num_zombies):
		zombies = []
		for i in range(num_zombies):
			zombies.append(Zombie())
		return zombies
     




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
      
	
	def spawn_zombies(self, num_zombies):
		if Prize.distance(p1) < 20:
			zombies = []
			for i in range(num_zombies):
				zombies.append(Zombie())
			return zombies

	def die(self):
		self.clear()
		self.ht()
		self.alive = False


class Bomb(Turtle):
	def __init__(self):
		super().__init__()
		self.speed(0)
		self.hideturtle()
		self.color(player_color)
		self.penup()
		self.goto(randint(-250, 250), randint(-250, 250))
		self.setheading(randint(0,360))
		  

	def relocate(self):
		self.goto(randint(-250, 250), randint(-250, 250))
		self.setheading(randint(0,360))



'''
Bullet() Class
Constructor ( def __init__(self) ):
- Input: player object
- Attributes:
	- Position: same as player
	- Heading: same as player
	- Player: the player
 
move(self):
- move 15 or more pixels forward
- should call on the die() method when the bullet leaves the playing area

die()
- hides the object. 
- removes object from the player's bullet list
'''


#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")

playing_area()


screen.mainloop()
