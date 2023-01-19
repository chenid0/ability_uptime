from random import random, seed

# seed random number generator
seed(1)

ability_active = False
active_end_rounds = 0
active_start_rounds = 0
num_iters = 100000
num_rounds = 10
# num_rounds = 10

ability_chance = .5  # probability of ability triggering
ability_duration = 2  # number of rounds it is active once triggered
ability_stack = 0
ability_num_weapons_pre_procs = 1
ability_num_weapons_during_procs = 3
ability_num_weapons_post_procs = 1
ability_num_shots_per_weapons = 1

starting_crit_rate = .22
crit_increase_proc = .5

total_num_stacks = 0
total_num_stacks_check = 0
total_crit_rate = 0.0

for i in range(num_iters):
    round_fall_off = [0] * 100
    ability_stack = 0
    crit_rate = starting_crit_rate

    for combat_round in range(num_rounds):
        #print(f"\nround {combat_round+1}")
        dec_amt = round_fall_off[combat_round]
        ability_stack -= dec_amt
        #print(f"cur num stacks {ability_stack}")
        #print(f"num stacks falling off: {dec_amt}")
        ability_proc = False

        # print(first_ability_chances_start_index)
        # calculate first shot of round without any proc boost
        crit_rate = min((ability_stack * .5) + starting_crit_rate, 1)
        for weapon in range(ability_num_weapons_pre_procs):
            total_crit_rate += crit_rate
            total_num_stacks_check += 1

        for chance in range(ability_num_weapons_during_procs - 1):
            for shot in range(ability_num_shots_per_weapons):
                first_ability_roll = random()  # generate random numbers between 0-1
                #print(f"first ability roll {first_ability_roll}")
                if first_ability_roll <= ability_chance:
                    ability_proc = True

            if ability_proc:
                ability_stack += 1
                #print(f"stack will fall off in round {combat_round+ability_duration}")
                round_fall_off[combat_round+ability_duration] += 1
                total_num_stacks += ability_stack
                crit_rate = min((ability_stack *.5) + starting_crit_rate, 1)
                total_crit_rate += crit_rate
                #print(f"activating for {ability_duration} rounds ")
                #print(f" cur num stacks {ability_stack}")
            else:
                #print(f"ability did not activate cur num stacks {ability_stack}")
                pass
            for weapon in range(ability_num_weapons_post_procs):
                total_crit_rate += crit_rate
                total_num_stacks_check += 1


print(f"number of rounds = {num_rounds}")
print(f"base crit rate = {starting_crit_rate}")
print(f"num incoming weapons per round = {ability_num_weapons_during_procs}")
print(f"num incoming shots per weapons= {ability_num_shots_per_weapons}")
print(f"% chance to proc = {ability_chance}")
#print(f"{num_iters} iterations")
#print(f"{total_num_stacks}")
#print(f"{total_num_stacks_check}")
#print(f"average num stacks for weapon fire = {total_num_stacks / total_num_stacks_check}")
print(f"average crit rate  for weapon fire = {total_crit_rate / total_num_stacks_check}")



