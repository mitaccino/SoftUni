deck = input().split()
shuffles = int(input())

left_half = []
right_half = []

for s in range(shuffles):
    curr_deck = []
    half = int(len(deck) / 2)
    left_half = deck[0:half]
    right_half = deck[half::]
    for card in range(len(left_half)):
        curr_deck.append(left_half[card])
        curr_deck.append(right_half[card])
    deck = curr_deck
print(deck)
