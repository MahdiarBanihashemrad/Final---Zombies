from turtle import *
from random import randint, choice
import time

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

class Score(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.speed(0)
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def increase(self):
        self.score += 1
        self.display_score()

class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key, bomb_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.player_color = color
        self.penup()
        self.bombs = []
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)
        screen.onkey(self.drop_bomb, bomb_key)

    def fire(self):
        if len(self.bullets) < 5:
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
            self.ht()
            self.alive = False

    def drop_bomb(self):
        if len(self.bombs) < 3:
            bomb = Bomb(self)
            self.bombs.append(bomb)

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
		self.speed(0)
		self.shapesize(2)
		self.shape("circle")
		self.color("yellow")
		self.penup()
		self.goto(randint(-250, 250), randint(-250, 250))

	def relocate(self):
		self.goto(randint(-250, 250), randint(-250, 250))

	def move(self):
		
		newX = randint(-3, 3) + self.xcor()
		newY = randint(-3, 3) + self.ycor()
		
		if newX >250 or newX <-250:
			newX = self.xcor()

		if newY >250 or newY < -250:
			newY = self.ycor()

		self.goto(newX, newY)

class Zombie(Turtle):
    def __init__(self, target_player):
        super().__init__()
        self.speed(0)
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.target = target_player
        self.goto(randint(-240, 240), randint(-240, 240))

    def move(self):
        self.setheading(self.towards(self.target))
        self.forward(randint(2, 3))

    def die(self):
        self.clear()
        self.ht()


class Bomb(Turtle):
    def __init__(self, player):
        print("Bomb")
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.color('red')
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.player = player
        self.screen = player.getscreen()
        self.blast_radius = 100
        self.screen.ontimer(self.explode, 1000)
        self.showturtle()
            
	

    def explode(self):
        self.showturtle()
        self.shape("circle")
        self.shapesize(self.blast_radius / 10)


        zombies_to_remove = []
        for z in zombies:
            if self.distance(z) < self.blast_radius:
                z.die()
                zombies_to_remove.append(z)

        for z in zombies_to_remove:
            zombies.remove(z)
        
        screen.ontimer(self.clear_explosion, 500)
        
        

    def clear_explosion(self):
        print("Cleared")
        self.clear()
        self.hideturtle()
        if self in self.player.bombs:
            self.player.bombs.remove(self)
        




def update():
    global zombies, running
    
    if not running:
        return

    if not p1.alive:
        game_over("Player 2 Wins! Player 1 was eaten.")
        return
    if not p2.alive:
        game_over("Player 1 Wins! Player 2 was eaten.")
        return

    if p1.alive and p2.alive:

        p1.move()
        p2.move()


        for bullet in p1.bullets[:]:
            bullet.move()
            
            for zombie in zombies[:]:
                if bullet.distance(zombie) < 15:
                    bullet.die()
                    zombie.die()
                    zombies.remove(zombie)
                    score1.increase()

        for bullet in p2.bullets[:]:
            bullet.move()
            
            for zombie in zombies[:]:
                if bullet.distance(zombie) < 15:
                    bullet.die()
                    zombie.die()
                    zombies.remove(zombie)
                    score2.increase()

        
        prize.move()
        prize_touched = False

        if p1.distance(prize) < 20:
            prize_touched = True
            score1.increase()
        elif p2.distance(prize) < 20:
            prize_touched = True
            score2.increase()

        if prize_touched == True:
            prize.relocate()
            global spawn_count
            spawn_count += 2
            for i in range(spawn_count // 2):
                zombies.append(Zombie(p1))
                zombies.append(Zombie(p2))

        for zombie in zombies:
            zombie.move()
            if zombie.distance(p1) < 20:
                p1.kill_turtle()
            if zombie.distance(p2) < 20:
                p2.kill_turtle()
    time.sleep(0.01)
    screen.ontimer(update, 30)

def game_over(message):
    global running
    running = False
    pen = Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.write(message)


#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.onkey(update, "space")

p1 = Player(-100, 0, "blue", screen, "d", "a", "w", "q")
p2 = Player(100,0,"red",screen, "Right","Left", 'Up', "m")
prize = Prize()

playing_area()


score1 = Score(-100, 260, 'blue')
score2 = Score(100, 260, 'red')

p1 = Player(-100, 0, "blue", screen, "d", "a", "w", 'q')
p2 = Player(100,0,"red",screen, "Right","Left", 'Up', 'm')
zombies = []
prize = Prize()
spawn_count = 2



zombies.append(Zombie(p1))
zombies.append(Zombie(p2))

running = True


screen.mainloop()
