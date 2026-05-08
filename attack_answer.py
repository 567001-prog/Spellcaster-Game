
import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0) 
wn.bgpic("output-onlinepngtools (2).gif")

pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")

def start():
    name = wn.textinput("Name Entry", "What is your name?")
    
    if name is None:
        name = "loser"

    pen.goto(0, 100)
    
    intro_text = [
        f"Hello, {name}! Your Kingdom is under attack.",
        "You must defeat the monsters to save the kingdom. ",
        "To fight the monster you must unscramble the spell and type",
        "it into the text box before the time runs out.",
        "There are 4 monsters headed your way.",
        "Good luck!"
    ]

    current_y = 100
    for line in intro_text:
        pen.goto(0, current_y)
        pen.write(line, align="center", font=("Times New Roman", 25, "bold"))
        current_y -= 30
start()

wn.mainloop()

