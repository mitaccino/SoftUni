cards = input().split()

a = [int(card[2:]) for card in cards if card[0] == 'A']
b = [int(card[2:]) for card in cards if card[0] == 'B']

a_count = 11 - len(set(a))
b_count = 11 - len(set(b))

game_terminate = False

print(f"Team A - {a_count}; Team B - {b_count}")
if a_count < 7 or b_count < 7:
    game_terminate = True
    break


    print("Game was terminated")

