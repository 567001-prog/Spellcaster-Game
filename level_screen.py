import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgcolor("navy")

pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")

def next_screen():
  pen.clear()
  #put next screen here!! :)

def show_level_screen(level_number):
  pen.clear()
  pen.goto(0, 0)
  pen.write(f"Level {level_number}", align="center", font=("Times New Roman", 60, "bold"))
  pen.goto(0, -90)
  pen.write(f"Press '{level_number}' to Start", align="center", font=("Times New Roman", 20, "normal"))
  wn.listen()
  #got rid of the on key

# example: show_level_screen(5)

wn.mainloop()
