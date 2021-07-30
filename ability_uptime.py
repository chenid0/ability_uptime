from random import random, seed

# seed random number generator
seed(1)

ability_active = False
active_rounds = 0
num_rounds = 100_000_000
# num_rounds = 1000
cur_ability_duration = 0

first_ability_chance = 0.8  # probability of ability triggering
first_ability_duration = 3  # number of rounds it is active once triggered
first_ability_num_chances = [1]  # number of times it can trigger in a round
first_ability_chances_start_index = 0

second_ability_chance = 0.5  # probability of ability triggering
second_ability_duration = 2  # number of rounds it is active once triggered
second_ability_num_chances = [3, 2, 2]  # number of times it can trigger in a round
second_ability_chances_start_index = 2

oblit_activate = 0
oblit_not_activate = 0
for round in range(num_rounds):
    #print(f"round {round+1}")
    cur_ability_duration -= 1
    if cur_ability_duration <= 0:
        ability_active = False
    if ability_active:
        # print("ability already active")
        pass

    # print("ability not active")
    # print(first_ability_chances_start_index)
    num_chances = first_ability_num_chances[first_ability_chances_start_index]
    for _ in range(num_chances):
        first_ability_roll = random()  # generate random numbers between 0-1
        # print(f"first ability roll {first_ability_roll}")
        if not ability_active and first_ability_roll <= first_ability_chance:
            ability_active = True
            cur_ability_duration = first_ability_duration
            # print(f"activating for {ability_duration} rounds ")

    # second officer nero
    num_chances2 = second_ability_num_chances[second_ability_chances_start_index]
    #print(num_chances2)
    first = True
    for _ in range(num_chances2):
        second_ability_roll = random()
        # print(f"second ability roll {second_ability_roll}")
        if not ability_active and second_ability_roll <= second_ability_chance:
            ability_active = True
            cur_ability_duration = second_ability_duration
            # print(f"activating for {ability_duration} rounds ")
        if ability_active and second_ability_chances_start_index == 0 and first:
            oblit_activate += 1
        elif num_chances2 == 3 and first:
            oblit_not_activate += 1
        first = False

    first_ability_chances_start_index += 1
    first_ability_chances_start_index = first_ability_chances_start_index % len(
        first_ability_num_chances
    )
    # increment firing pattern index
    second_ability_chances_start_index += 1
    second_ability_chances_start_index = second_ability_chances_start_index % len(
        second_ability_num_chances
    )
    # print(f"ability active t/f: {ability_active}")
    if ability_active:
        active_rounds += 1
    # print(f"total num rounds active: {active_rounds}")
    # print(f"number of remaining rounds active: {ability_duration-1}")

print(active_rounds / num_rounds)
print(oblit_activate / (oblit_activate + oblit_not_activate))

