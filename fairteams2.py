import random
from time import sleep
delay = 0.78

# Enter the top 2 players into 'best', the 3rd and 4th best players into 'middle' and all other players 
# into 'everyoneelse'

best = ['Chris', 'Joe']
middle = ['Jonny', 'Eloka']
everyoneelse = ['Dandy', 'Mandy', 'Glenn', 'Tom', 'Luke S', 'Marc', 'Rob', 'Dave Cody']

# makes sure that all players in the lists above are selected (numbers in the below variables should 
# equal the number of names in the respective list)

countofbest = 2
countofmiddle = 2
countofeveryoneelse = 8                           

# selects players from each list. As long as the number of players in each of the lists 'best', 'middle', 
# and 'everyoneelse' matches the numbers defined in 'countofbest', 'countofmiddle' and, 'countofeveryoneelse', then no player will be
# left unselected

randomeveryoneelse = random.sample(everyoneelse, countofeveryoneelse)
randombest = random.sample(best, countofbest)
randommiddle = random.sample(middle, countofmiddle)

# uses the 
team1 = [randomeveryoneelse[0], randomeveryoneelse[1], randomeveryoneelse[2], randomeveryoneelse[3], randommiddle[0], randombest[0]]
team2 = [randomeveryoneelse[4], randomeveryoneelse[5], randomeveryoneelse[6], randomeveryoneelse[7], randommiddle[1], randombest[1]]
print("Loading players into database.."); sleep(delay*2)
print("Running selection algorithm.."); sleep(delay*2)
print("Analysis complete"); sleep(delay*2)
print("The teams are:"); sleep(delay*2)
print("")
print("Team 1: "); print(*team1, sep = ', ')
print("")
print("Team 2: "); print(*team2, sep = ', '); sleep(delay*2)
print("")
print("Score Predictor: Team 1 TEN Team 2 NINE"); sleep(delay*2)
print("")
print("The team selection computer's decision is final")
sleep(delay*4)

