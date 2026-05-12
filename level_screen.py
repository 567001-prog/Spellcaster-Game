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
    #add the next screen here :)

def show_level_screen():
  pen.goto(0, 0)
  pen.write("Level 1", align="center", font=("Times New Roman", 60, "bold"))
  
  pen.goto(0, -90)
  pen.write("Press '1' to Start", align="center", font=("Times New Roman", 20, "normal"))

show_level_screen()

wn.listen()
wn.mainloop()
