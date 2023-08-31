import random
numberOfStreaks = 0
sides = []
for coin in range(0, 10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    if random.randint(0,1) == 0:
        sides.append('T')
    else:
        sides.append('H')
    # Code that checks if there is a streak of 6 heads or tails in a row.
try:

    for i in range(0, 10000):
        if sides[i] == 'T':
         if sides[i+1] == 'T':
             if sides[i+2] == 'T':
                  if sides[i+3] == 'T':
                     if sides[i+4] == 'T':
                         if sides[i+5] == 'T':
                              numberOfStreaks += 1
        if sides[i] == 'H':
            if sides[i+1] == 'H':
                if sides[i+2] == 'H':
                    if sides[i+3] == 'H':
                        if sides[i+4] == 'H':
                            if sides[i+5] == 'H':
                                numberOfStreaks += 1

except IndexError:

 print(f"chance of getting 6 streaks is {(numberOfStreaks/100)*100} %")




