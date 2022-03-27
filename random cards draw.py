# import modules
import itertools,random

# make a dck of cards

deck=list(itertools.product(range(1,14),['Spade','Diamond','Heart','Club']))

# SHUFFLE THE CARDS
random.shuffle(deck)

#Draw 5 cards
print("You got: ")
for i in range(52):
    print(deck[i][0], "of", deck[i][1])
