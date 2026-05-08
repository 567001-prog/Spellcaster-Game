import random

fire_damage = 15
water_damage = 12
earth_damage = 20
wind_damage = 8
ice_damage = 18

elements = ["fire", "water", "earth", "wind", "ice"]
element_damages = [fire_damage, water_damage, earth_damage, wind_damage, ice_damage]

# attack types + how much they multiply damage
attack_types = ["fist", "dagger", "ball", "beam"]
attack_multipliers = [1.0, 1.4, 1.6, 1.8]

def random_attack():
    # pick random element
    rand_index = random.randint(0, len(elements) - 1)
    element = elements[rand_index]
    base_damage = element_damages[rand_index]

    # pick random attack type
    rand_index2 = random.randint(0, len(attack_types) - 1)
    attack = attack_types[rand_index2]
    multiplier = attack_multipliers[rand_index2]

    spell_name = element + " " + attack  # ex: "fire dagger"

    # calculate damage
    damage = base_damage * multiplier
    damage = int(damage)  # remove decimal

    return spell_name, damage
  
