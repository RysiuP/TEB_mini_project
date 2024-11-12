import random
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard['Color'] = color
        allCards.append(aCard)

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

max = len(allCards)
for i in range(0,max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1['Power'] == card2['Power']:
        player1.append(card1)
        player2.append(card2)
        print('=EQUAL \t %d \t %d \t' % (card1['Power'],card2['Power']) + len(player1) * '*')
    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1['Power'],card2['Power']) + len(player1) * '*')
    else:
        player2.append(card1)
        player2.append(card2)
        print('PLAY-2 \t %d \t %d \t' % (card1['Power'],card2['Power']) + len(player1) * '*')

if len(player1) > 0:
    print('Wygrał gracz 1!')
else:
    print('Wygrał gracz 2!')

