import random

def random_flips(number_of_times):
    list_of_flips = []
    for flip in range(1, number_of_times):
        flip = random.randint(0, 1)
        if flip == 0:
            list_of_flips.append("H")
        else:
            list_of_flips.append("T")
    flippers = "".join(list_of_flips)
    return flippers

print("How many times do you want to flip the coin? ")
no_of_flips = int(input())
flips = random_flips(no_of_flips)
print(flips)

def number_of_streaks(list):
    global no_of_flips
    heads_count = flips.count("HHHHHH")
    tails_count = flips.count("TTTTTT")
    head_details = f"""
There are {heads_count} streaks of HEADS when a coin is flipped {no_of_flips} times"""
    tail_details = f"There are {tails_count} streaks of TAILS when a coin is flipped {no_of_flips} times"
    return head_details, tail_details

no_of_head_streaks, no_of_tail_streaks = number_of_streaks(flips)
print(no_of_head_streaks)
print(no_of_tail_streaks)