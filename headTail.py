import random
numberOfStreak = 0
collection = []
headcount, tailcount =0,0
for i in range(1000):
    rando = random.randint(0,1)
    if rando:
        collection.append('H')
        headcount+=1
        tailcount=0
    else:
        collection.append('T')
        tailcount+=1
        headcount=0
    if headcount ==6 or tailcount==6:
        numberOfStreak+=1
print('Chance of streak per 10000 flips = ', numberOfStreak)
