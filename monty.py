import random 
from random import shuffle, randint
def game(contestant_switch):
    prizes = ["goat", "goat", "car"]
    random.shuffle(prizes)
    original_choice = prizes[randint(0, 2)] # either "goat" or "car"
    prizes.remove(original_choice)
    prizes.remove("goat") # Prizes is now a single-item list
    if(contestant_switch):
        return prizes[0]
    else:
        return original_choice

score = 0

def play(trials, switch):
    score = 0
    for i in range(trials):
        prize = game(switch)
        if(prize == 'car'):
            score += 1
    return score / trials;

n = 100000
def get_numeric():
    while True:
        try: 
            return int(input(f"Number of iterations [{n}]:"))
        except ValueError:
            return n

score = 0
print("Monty Hall Simulation")
print("")
switch = input("Should the player switch? Y/n")
if(switch == 'n'):
    switch_strategy = False
else:
    switch_strategy = True
trials = get_numeric()
s = ""
if(switch_strategy is False):
   s = " not"
percentage = play(trials, switch_strategy)
print(f"Running simulation: {trials} games; Player does{s} switch.")
print(f"Result: {percentage * 100.0}% games won.")
