from random import random, seed

# seed random number generator
seed(1)

ability_active = False
active_rounds = 0
num_rounds = 100_000_000
ability_duration = 0
first_ability_chance = 0.8
first_ability_duration = 3

second_ability_chance = 0.5
second_ability_duration = 2
for round in range(num_rounds):
    # print(f"round {round+1}")
    ability_duration -= 1
    if ability_duration <= 0:
        ability_active = False
    if ability_active:
        # print("ability already active")
        pass
    else:
        # print("ability not active")
        first_ability_roll = random()  # generate random numbers between 0-1
        # print(f"first ability roll {first_ability_roll}")
        if first_ability_roll <= first_ability_chance:
            ability_active = True
            ability_duration = first_ability_duration
            # print(f"activating for {ability_duration} rounds ")
        if not ability_active:
            second_ability_roll = random()
            # print(f"second ability roll {second_ability_roll}")
            if second_ability_roll <= second_ability_chance:
                ability_active = True
                ability_duration = second_ability_duration
                # print(f"activating for {ability_duration} rounds ")
    # print(f"ability active t/f: {ability_active}")
    if ability_active:
        active_rounds += 1
    # print(f"total num rounds active: {active_rounds}")
    # print(f"number of remaining rounds active: {ability_duration-1}")

print(active_rounds / num_rounds)
