import turtle

# variable
screen = turtle.Screen()        
monster_health = 100            # change later
player_x = -200                 # The starting X coordinate for the attack
player_y = 0                    # The starting Y coordinate for the attack
monster_x = 200                 # The target X coordinate to move towards
monster_y = 0                   # The target Y coordinate to move towards
damage_amount = 10              # How much health the attack removes, randomize this part this later

def register_attack_images(game_screen):
    for i in range(1, 21):
        game_screen.register_shape(f"{i}.gif")

def attack(image_filename):
    projectile = turtle.Turtle()
    projectile.penup()
    projectile.hideturtle()       
    projectile.speed(0)           
    
    # player location
    projectile.goto(player_x, player_y) 
    
    # set to image
    projectile.shape(image_filename)
    projectile.showturtle()
    
    # animation for attack
    projectile.speed(1)         
    projectile.goto(monster_x, monster_y) # monster location
    
    projectile.hideturtle()
    
    # for monster health, change to variables
    # global monster_health
    # monster_health -= damage_amount
    # print(f"Hit! Monster health is now {monster_health}")


register_attack_images(screen)
attack("6.gif")

screen.mainloop()


