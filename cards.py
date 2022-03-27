import random

# LIST HOLDERS TO PLACE OUR CARDS IN THERE
cardfaces = []
suits = ["Heart","Diamonds","Clubs","Spade"]
royals = ["J","Q","K","A"]
deck = []

# USING LOOPS TO ADD OUR CONTENTS 
for i in range(2,11):
    cardfaces.append(str(i))    # THIS ADDS NUMBER 2 TO 10 IN THE THE STRING DATA
for j in range(4):
    cardfaces.append(royals[j]) # THIS ADDS THE ROYAL FACES TO THE CARDBASE
    
for k in range(4):
    for l in range(13):
        card = (cardfaces[l]+" of "+ suits[k])
        # THIS MAKES EACH CARD, CYCLING THROUGH SUITS, BUT FIRST THROUGH FACES
        deck.append(card)
# THIS ADDS THE INFORMATION TO THE "FULL DECK" WE WANT TO MAKE
# NOW LET'S SHUFFLE OUR DECK!!

# NOW LET'S SEE THE CARDS!!

cardfrom = int(input("Enter the card from: "))
cardTo = int(input("Enter the card to: "))
for m in range(cardfrom,cardTo+1):
    print(deck[m])
