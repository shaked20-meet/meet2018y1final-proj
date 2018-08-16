import turtle
import random
import time
#These are the frog's shape code lines.
turtle.register_shape("FROG.gif")
turtle.register_shape("bottle.gif")
frog = turtle.clone()
turtle.hideturtle()
turtle.bgpic("river.gif")
frog.penup()
frog.shape("FROG.gif")

turtle.tracer(1,0)
turtle.penup()
SQUARE_SIZE = 50

under_rock = False

#lists of positions
frog_pos = []
stone_pos = []

frog.goto(0,-200)

#directions functions & variables
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

rock_time = 0

UP_ARROW = "Up"
DOWN_ARROW = "Down"
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"

game_over = False

direction = UP

def up():
    global direction 
    direction=UP
    print("You pressed the up key!")
    move_frog()

direction = LEFT

def left():
    global direction, game_over, rock_time
    direction=LEFT
    print("You pressed the left key!")
    move_frog()

direction = DOWN

def down():
    global direction
    direction = DOWN
    print("You pressed the down key!")
    move_frog()

direction = RIGHT

def right():
    global direction
    direction=RIGHT
    print("You pressed the right key!")
    move_frog()

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

#def trashfall():
    




#this function moves the frog to each position using 'SQUARE_SIZE' and direction.
def move_frog():
    global under_rock
    global direction, game_over
    global SQUARE_SIZE
    global frog_pos
    my_frog_pos = frog.pos()
    frog_pos.append(my_frog_pos)
    x_pos = my_frog_pos[0]
    
    y_pos = my_frog_pos[1] 

    if game_over:
        print("Game over!")
        print("good job!")
 

    if direction == UP:
        frog.goto(x_pos , y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction == DOWN:
        frog.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved up!")
    elif direction == LEFT:
        frog.goto(x_pos - SQUARE_SIZE,y_pos)  
        print("You moved left!")
    elif direction == RIGHT:
        frog.goto(x_pos + SQUARE_SIZE, y_pos)


#Edges, if the frog is outside, the game will be over.
    UP_EDGE = 250
    DOWN_EDGE = -250
    RIGHT_EDGE = 250
    LEFT_EDGE = -250

    if x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    if x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()
    if y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()


turtle.register_shape("stone.gif")
stone = turtle.clone()
stone.shape("stone.gif")

stone_pos = [(100, 100), (-100, 100), (-100, -100), (100, -100)]
stone_stamps = []

for this_stone_pos in stone_pos:

    stone.goto(this_stone_pos)
    stone1 = stone.stamp()
    stone_stamps.append(stone1)
    stone.hideturtle()

trash = turtle.clone()
trash.showturtle()
trash.shape("bottle.gif")
rand_x_pos = random.randint(-5, 5)*50
trash.goto(rand_x_pos, 250)

trash2 = turtle.clone()
trash2.showturtle()
trash2.shape("bottle.gif")
rand_x_pos = random.randint(-5, 5)*50
trash2.goto(rand_x_pos, 250)

trash3 = turtle.clone()
trash3.showturtle()
trash3.shape("bottle.gif")
rand_x_pos = random.randint(-5, 5)*50
trash3.goto(rand_x_pos, 250)

trash4 = turtle.clone()
trash4.showturtle()
trash4.shape("bottle.gif")
rand_x_pos = random.randint(-5, 5)*50
trash4.goto(rand_x_pos, 250)

trash_counter = 0

def trash_fall():
    global trash_counter, trash, trash2, trash3, trash4, rock_time, under_rock
    # trash 1
    x_pos = trash.pos()[0]
    y_pos = trash.pos()[1]
    trash.goto(x_pos, y_pos - 20)

    # trash 2
    x_pos2 = trash2.pos()[0]
    y_pos2 = trash2.pos()[1]
    trash2.goto(x_pos2, y_pos2 - 30)
    
    # trash 3
    
    x_pos3 = trash3.pos()[0]
    y_pos3 = trash3.pos()[1]
    trash3.goto(x_pos3, y_pos3 - 40)
    
    # trash 4
    x_pos4 = trash4.pos()[0]
    y_pos4 = trash4.pos()[1]
    trash4.goto(x_pos4, y_pos4 - 50)

    if frog.pos() in stone_pos:
        if rock_time == 0:
            rock_time = time.time()
            under_rock = True            
        elif time.time() - rock_time > 3:
            print("time's up go somewhere else stupido")
            stone_ind=stone_pos.index(frog.pos())
            stone.clearstamp(stone_stamps[stone_ind])
            stone_pos.pop(stone_ind)
            stone_stamps.pop(stone_ind)
            rock_time = 0
            under_rock = False

    if trash_counter == 80:
        turtle.write("YOU WON", align='center', font = ("Impact",30,"normal"))
        time.sleep(60)
        print("You won!")
        quit()
    if x_pos == frog.pos()[0] and abs(y_pos - frog.pos()[1]) < 20:
        if not under_rock:
            print("You got hit by the trash!")
            turtle.write("You got hit by the trash!", align='center', font = ("Impact",30,"normal"))
            time.sleep(2)
            quit()
    elif x_pos2 == frog.pos()[0] and abs(y_pos2 - frog.pos()[1]) < 20:
        if not under_rock:
            print("You got hit by the trash!")
            turtle.write("You got hit by the trash!", align='center', font = ("Impact",30,"normal"))
            time.sleep(2)
            quit()
    elif x_pos3 == frog.pos()[0] and abs(y_pos3 - frog.pos()[1]) < 20:
        if not under_rock:
            print("You got hit by the trash!")
            turtle.write("You got hit by the trash!", align='center', font = ("Impact",30,"normal"))
            time.sleep(2)
            quit()
    elif x_pos4 == frog.pos()[0] and abs(y_pos4 - frog.pos()[1]) < 20:
        if not under_rock:
            print("You got hit by the trash!")
            turtle.write("You got hit by the trash!", align='center', font = ("Impact",30,"normal"))
            time.sleep(2)
            quit()
    if y_pos < -250:
        trash_counter += 1
        trash.hideturtle()
        rand_x_pos = random.randint(-5, 5)*50
        trash.goto(rand_x_pos, 250)
        trash.showturtle()
        
    if y_pos2 < -250:
        trash_counter += 1
        trash2.hideturtle()
        rand_x_pos = random.randint(-5, 5)*50
        trash2.goto(rand_x_pos, 250)
        trash2.showturtle()

    if y_pos3 < -250:
        trash_counter += 1
        trash3.hideturtle()
        rand_x_pos = random.randint(-5, 5)*50
        trash3.goto(rand_x_pos, 250)
        trash3.showturtle()

    if y_pos4 < -250:
        trash_counter += 1
        trash4.hideturtle()
        rand_x_pos = random.randint(-5, 5)*50
        trash4.goto(rand_x_pos, 250)
        trash4.showturtle()
        
    turtle.ontimer(trash_fall, 100)
    
    
trash_fall()



    
        
        





    
  
   
