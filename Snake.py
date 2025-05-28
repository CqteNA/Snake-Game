import turtle as t
import random
import pickle

t.speed(0)
t.hideturtle()
t.penup()
t.goto(-200, 200)
t.pendown()
t.forward(400)
t.right(90)
t.forward(400)
t.right(90)
t.forward(400)
t.right(90)
t.forward(400)
t.penup()
t.goto(0, 0)

snake = t.Turtle()
snake.penup()
snake.hideturtle()
snake.speed(0)
snake.shape('square')

food = t.Turtle()
food.penup()
food.hideturtle()
food.speed(0)
food.shape('turtle')

start_game = False

text = t.Turtle()
text.penup()
text.hideturtle()
text.speed(0)
text.write("Press Space to Start!",
           align="center",
           font=("Comic Sans MS", 20, "bold"))

score_turtle = t.Turtle()
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.setpos(180, 200)  
score_turtle.write("Score: 0", align="center", font=("Comic Sans MS", 25, "bold"))  

high_score_file = "high_score.txt"

def load_high_score():
    try:
        with open("highscore.txt", "rb") as file:
            high_score = pickle.load(file)
            return high_score
    except (EOFError, FileNotFoundError):
        return 0  

def save_high_score(score):
    with open(high_score_file, "wb") as file:
        pickle.dump(score, file)

def place_food():
    food.hideturtle()
    food.setpos(random.randint(-180, 180), random.randint(-180, 180))
    food.showturtle()

def outside():
    left_wall = -200
    right_wall = 200
    bottom_wall = -200
    top_wall = 200
    (x, y) = snake.position()
    out = x > right_wall or y > top_wall or y < bottom_wall or x < left_wall
    return out

def game_over(score):
    snake.hideturtle()
    food.hideturtle()
    text.clear()
    text.write("Game Over!!!",
               align="center",
               font=("Comic Sans MS", 25, "bold"))
    return score

def display_score(score):
    score_turtle.clear()
    score_turtle.setpos(180, 200)
    score_turtle.write(f"Score: {score}", align="center", font=("Comic Sans MS", 25, "bold"))

def display_high_score(high_score):
    score_turtle.clear()
    score_turtle.setpos(-180, 200)
    score_turtle.write(f"High Score: {high_score}", align="center", font=("Comic Sans MS", 15, "bold"))

def start_the_game():
    global start_game, high_score
    if start_game:
        return
    start_game = True
    text.clear()
    score = 0
    snake_speed = 1
    place_food()
    display_score(score)
    snake.showturtle()
    while True:
        snake.forward(snake_speed)
        if snake.distance(food) < 20:
            score += 1
            snake_speed += 0.25
            place_food()
            display_score(score)
            if score > high_score:
                high_score = score
                display_high_score(high_score)
        if outside():
            score = game_over(score)
            break

def move_up():
    if snake.heading() == 180 or snake.heading() == 0 or snake.heading() == 270:
        snake.setheading(90)

def move_down():
    if snake.heading() == 180 or snake.heading() == 0 or snake.heading() == 90:
        snake.setheading(270)

def move_left():
    if snake.heading() == 90 or snake.heading() == 0 or snake.heading() == 270:
        snake.setheading(180)

def move_right():
    if snake.heading() == 180 or snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

window = t.Screen()

window.onkey(move_up, 'Up')
window.onkey(move_up, 'w')
window.onkey(move_down, 'Down')
window.onkey(move_down, 's')
window.onkey(move_left, 'Left')
window.onkey(move_left, 'a')
window.onkey(move_right, 'Right')
window.onkey(move_right, 'd')
window.onkey(start_the_game, 'space') 
window.listen()

high_score = load_high_score()  
display_high_score(high_score)

t.mainloop()
