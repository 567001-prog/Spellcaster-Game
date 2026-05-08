import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("output-onlinepngtools (2).gif")

pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")


def clear_text():
  pen.clear()


def start():
  name = wn.textinput("Name Entry", "What is your name?")

  if name is None:
    name = "loser"

  intro_text = [
    f"Hello, {name}! Your kingdom is under attack.",
    "You must defeat the monsters to save the kingdom.",
    "Unscramble the spell before time runs out.",
    "There are 4 monsters headed your way.",
    "Press 'c' to continue.",
    "Good luck!"
  ]

  current_y = 120

  for line in intro_text:
    pen.goto(0, current_y)

  pen.write(
    line,
    align="center",
    font=("Times New Roman", 25, "bold")
  )

  current_y -= 50

start()
wn.listen()
wn.onkey(clear_text, "c")

wn.mainloop()
