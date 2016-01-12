import random

def roll(s,r):
    rolls = []
    for i in range(s):
        rolls.append(0)
    print rolls
    for i in range(0, r):
        die = random.randint(1,s)
        rolls[die - 1]+=1
    return rolls
print roll(20,20)

