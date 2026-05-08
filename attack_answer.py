"""Function attack_answer: Scramble the attack string and show on the screen. 
Add timer above the word. Wait for user input of the correct or incorrect word,
and attack or don't

def attack_answer():

    #scramble element & attack string
    ele = list(element)
    random.shuffle(ele)
    ''.join(ele)

    repeat for attack string

    scrambled_full = join scrambled attack and element
    display on screen
    answer = input("Unscrambled: ")
    add timer
    every second check:
        if timer is out:
            attack function doesn't run
            word and timer disapears
        elif answer = scrambled_ful:
            word and timer disapears
            attack()
"""
# SETUP ----------------------------
import random as r
import turtle as t
import threading
import time

wn = t.Screen()
wn.setup(600, 400)

counter =  t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(0, 0) 
counter.pendown()

writer = t.Turtle()
writer.penup()

# VARIABLES ----------------------
element = 'fire'
attack = 'ball'
attempt = ''
full_attack = 'fire ball'

timer = 30
counter_interval = 1000 
timer_up = False
correctness = False          # this is temp, does not matter


# FUNCTIONS ----------------------
def countdown():
  global timer, timer_up
  while timer > 0 and not timer_up:
    print("\rTimer: " + str(timer) + "  ", end='', flush=True)
    timer -= 1
    time.sleep(1)
  if not timer_up:
    print("\rTime's Up!      ", flush=True)
    timer_up = True

def update_score():
  global correctness
  correctness = True

# check if the user's answer is correct 
# + what happens when the user types correct or incorrect answer
def check_answer():
  global timer_up, attempt, full_attack
  if (attempt == full_attack):
    writer.clear()
    writer.penup()
    writer.forward(-50)
    writer.write('Attack!', font=('Book Antiqua', 24, 'normal'))
    timer_up = True
    update_score()
    print('Correct') # REPLACE WITH THE ATTACK FUNCTION
  else:
    attempt = input('Try again: ')
    check_answer()

# shuffles answer and waits for the user to type in the incorrect or correct answer
def attack_answer():
    global attempt

    #scramble element and attack
    ele = list(element)
    r.shuffle(ele)
    shuf_ele = ''.join(ele)

    ata = list(attack)
    r.shuffle(ata)
    shuf_ata = ''.join(ata)

    shuf_full = shuf_ele + ' ' + shuf_ata

    writer.penup()
    writer.hideturtle()
    writer.goto(0, 100)
    writer.write(shuf_full, align = 'center', font = ('Book Antiqua', 24, 'normal'))

    threading.Thread(target=countdown, daemon=True).start()

    attempt = input('')

    if not timer_up:
        check_answer()

    

# CALLS --------------------------
attack_answer()

wn.mainloop()