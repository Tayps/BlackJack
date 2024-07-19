import random as rand
import numpy as np

# Create Deck
deck = []
deck = []
for i in range(1,14):
    i = str(i)
    if i == '1':
        i = 'Ace'
    elif i == '11':
        i = 'Jack'
    elif i == '12':
        i = 'Queen'
    elif i == '13':
        i = 'King'
    else:
        i=i
    for j in ['\U00002665', '\U00002663', '\U00002666', '\U00002660']:
        deck.append(i + ' ' + j)
# Create gameDeck
gameDeck = []

#Create cut card
cut = 'cut' 

# Assign values for cards
cardValue = {}

for i in deck:
    if 'Ace' in i:
        value = 1
    elif [a for a in ['Jack', 'Queen', 'King'] if(a in i)]:
        value = 10
    else:
        value = int(i[0:2])

    cardValue[i] = value

def shoe():
    global gameDeck
    print("Number of Decks?", end="\n\n") 
    n = input() # User chooses number of decks
    gameDeck = list(np.repeat(deck, n)) # Duplicate number of decks by user's choice 
    rand.shuffle(gameDeck) # Shuffle the deck
    gameDeck.insert(rand.randrange(len(gameDeck)-5),cut) #insert cut card at random position in deck.
    
# Dealing a Hand
def dealCards():
    dealerHand.append(gameDeck.pop(0))
    playerHand.append(gameDeck.pop(0))
    dealerHand.append(gameDeck.pop(0))
    playerHand.append(gameDeck.pop(0))
    
# Drawing a card
def drawCard(char):
    if char == 'player':
        playerHand.append(gameDeck.pop(0))
    elif char == 'dealer':
        dealerHand.append(gameDeck.pop(0))
    

# Calculate hand value
def handValue(char):
    ace = ['Ace \U00002665', 'Ace \U00002663', 'Ace \U00002666', 'Ace \U00002660']
    global playerHand
    global dealerHand
    global dealerValue 
    global playerValue 
    if char == 'dealer':
        if any(a in dealerHand for a in ace) == True:
            if len(dealerHand) == 2:
                dealerValue = sum([cardValue[x] for x in dealerHand])+10
            else:
                dealerValue = sum([cardValue[x] for x in dealerHand])    
        else:
            dealerValue = sum([cardValue[x] for x in dealerHand])
                
    elif char == 'player':
        if any(a in playerHand for a in ace) == True:
            if len(playerHand) == 2:
                playerValue = sum([cardValue[x] for x in playerHand])+10
            else:
                playerValue = sum([cardValue[x] for x in playerHand])
        else:
            playerValue = sum([cardValue[x] for x in playerHand])

# Start of Game
while True:
    endGame = False
    print("New Hand? [y/n]", end="\n\n")
    start = input()
    if start == 'y':
# Create player Hands
        dealerHand = []
        playerHand = []
# Create Shoe if deck is empty:
        if gameDeck == []:
            shoe()
        while True:    
            dealCards()
            if ((cut in dealerHand) or (cut in playerHand)):
                dealerHand.clear()
                playerHand.clear()
                shoe()
                continue
            break
    elif start == 'n':
        break

    handValue('player')
    handValue('dealer')

    if (playerValue == 21) and (dealerValue ==21):       
        print('Dealer Hand is:', dealerHand, sep = ' ')
        print('Player Hand is:', playerHand, sep = ' ', end="\n\n")
        print('Dealer ' + str(dealerValue) + ' vs Player ' + str(playerValue),end="\n\n")
        print('Both Players BlackJack.')
        print('PUSH!', end="\n\n")
        continue
        
    elif playerValue == 21:
        print('Dealer Hand is:', dealerHand, sep = ' ')
        print('Player Hand is:', playerHand, sep = ' ', end="\n\n")
        print('Dealer ' + str(dealerValue) + ' vs Player ' + str(playerValue),end="\n\n")
        print('Player BlackJack!', end="\n\n")
        continue
    
    elif dealerValue == 21:
        print('Dealer Hand is:', dealerHand, sep = ' ')
        print('Player Hand is:', playerHand, sep = ' ', end="\n\n")
        print('Dealer ' + str(dealerValue) + ' vs Player ' + str(playerValue),end="\n\n")  
        print('Dealer BlackJack!', end="\n\n")
        continue


    
    print("The dealer's face up card is: " + dealerHand[0])
    print("The player's cards are: " + playerHand[0] +" & " + playerHand[1], end="\n\n")
    # print("There are " + str(len(gameDeck)) + " cards left in the deck.", end="\n\n")

    while True:
        print("Player's move")
        print("1) Hit")
        print("2) Stand")
        move = input()
        if move == '1':
            drawCard('player')
            if ((cut in dealerHand) or (cut in playerHand)):
                print("Reshuffle Deck", end="\n\n")
                shoe()
                endGame = True
                break
                
            print("The player's cards are: ", playerHand, end="\n\n")
            handValue('player')
            if playerValue > 21:
                print('Dealer Hand is:', dealerHand, sep = ' ')
                print('Player Hand is:', playerHand, sep = ' ', end="\n\n")
                print('Dealer ' + str(dealerValue) + ' vs Player ' + str(playerValue),end="\n\n")
                print('Player Bust!', end="\n\n")
                endGame = True
                break
        elif move == '2':
            break
    if endGame == True:
        continue

    handValue('dealer')
    while dealerValue < 16:
        drawCard('dealer')
        if ((cut in dealerHand) or (cut in playerHand)):
            print("Reshuffle Deck", end="\n\n")
            shoe()
            endGame = True
            break
        handValue('dealer')
        if dealerValue > 21:
            print('Dealer Hand is:', dealerHand, sep = ' ')
            print('Player Hand is:', playerHand, sep = ' ', end="\n\n")
            print('Dealer ' + str(dealerValue) + ' vs Player ' + str(playerValue),end="\n\n")
            print('Dealer Bust!', end="\n\n")
            endGame = True
            break
            
    if endGame == True:
        continue
        
    handValue('player')

    print('Dealer ' + str(dealerValue) + ' vs Player ' + str(playerValue),end="\n\n")
    if dealerValue > playerValue:
        print('Dealer Hand is:', dealerHand, sep = ' ')
        print('Player Hand is:', playerHand, sep = ' ', end="\n\n")
        print('Dealer Wins', end="\n\n")
    elif playerValue > dealerValue:
        print('Dealer Hand is:', dealerHand, sep = ' ')
        print('Player Hand is:', playerHand, sep = ' ', end="\n\n")
        print('Player Wins', end="\n\n")
    else:
        print('Dealer Hand is:', dealerHand, sep = ' ')
        print('Player Hand is:', playerHand, sep = ' ', end="\n\n")
        print('Push', end="\n\n")

            