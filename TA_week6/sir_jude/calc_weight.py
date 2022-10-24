def calc_weight_on_planet(weight, gravity = 23.1):
    mass = weight / 9.8
    weight = mass * gravity
    print(weight)

calc_weight_on_planet(120)