import turtle as trtl

# variable
screen = trtl.Screen()          # change later
player_x = -200                 # The starting X coordinate for the attack
player_y = 0                    # The starting Y coordinate for the attack
monster_x = 200                 # The target X coordinate to move towards
monster_y = 0                   # The target Y coordinate to move towards
monster_health = 30


def register_attack_images(game_screen):
    for i in range(1, 21):
        game_screen.register_shape(f"{i}.gif")

def launch_attack(attack_name):
  global monster_health
  attack_value = 0
  projectile = trtl.Turtle()
  projectile.penup()
  projectile.hideturtle()
  projectile.speed(0)
  # player location
  projectile.goto(player_x, player_y) 
    
    # set to image
  if attack_name == 'fire ball':
    projectile.shape("1.gif")
    projectile.showturtle()
    attack_value = 20
  if attack_name == 'water ball':
    projectile.shape("2.gif")
    projectile.showturtle()
    attack_value = 20
  if attack_name == 'ice ball':
    projectile.shape("3.gif")
    projectile.showturtle()
    attack_value = 20
  if attack_name == 'wind ball':
    projectile.shape("4.gif")
    attack_value = 20
    projectile.showturtle()
  if attack_name == 'earth ball':
    projectile.shape("5.gif")
    attack_value = 20
    projectile.showturtle()
  if attack_name == 'fire beam':
    projectile.shape("6.gif")
    projectile.showturtle()
    attack_value = 20
  if attack_name == 'water beam':
    projectile.shape("7.gif")
    projectile.showturtle()
    attack_value = 20
  if attack_name == 'ice beam':
    projectile.shape("8.gif")
    projectile.showturtle()
    attack_value = 20
  if attack_name == 'wind beam':
    projectile.shape("9.gif")
    projectile.showturtle()
    attack_value = 20
  if attack_name == 'earth beam':
    projectile.shape("10.gif")
    projectile.showturtle()
    attack_value = 20
  if attack_name == 'fire fist':
    projectile.shape("11.gif")
    attack_value = 10
    projectile.showturtle()
  if attack_name == 'ice fist':
    projectile.shape("12.gif")
    projectile.showturtle()
    attack_value = 10
  if attack_name == 'water fist':
    projectile.shape("13.gif")
    projectile.showturtle()
    attack_value = 10
  if attack_name == 'wind fist':
    projectile.shape("14.gif")
    projectile.showturtle()
    attack_value = 10
  if attack_name == 'earth fist':
    projectile.shape("15.gif")
    projectile.showturtle()
    attack_value = 10
  if attack_name == 'water dagger':
    projectile.shape("16.gif")
    attack_value = 15
    projectile.showturtle()
  if attack_name == 'wind dagger':
    projectile.shape("17.gif")
    projectile.showturtle()
    attack_value = 15
  if attack_name == 'ice dagger':
    projectile.shape("18.gif")
    projectile.showturtle()
    attack_value = 15
  if attack_name == 'fire dagger':
    projectile.shape("19.gif")
    projectile.showturtle()
    attack_value = 15
  if attack_name == 'earth dagger':
    projectile.shape("20.gif")
    projectile.showturtle()
    attack_value = 15
    
    
    # animation for attack
  projectile.speed(1)         
  projectile.goto(monster_x, monster_y) # monster location
    
  projectile.hideturtle()
    
  monster_health -= attack_value
  print(f"Hit! Monster health is now {monster_health}")


register_attack_images(screen)
launch_attack("water ball")

screen.mainloop()
