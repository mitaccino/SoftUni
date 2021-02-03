gifts = input().split()
command = input()
while command != "No Money":
    curr_command = command.split()
    cur_gift = curr_command[1]
    if curr_command[0] == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == cur_gift:
                gifts[index] = "None"
    elif curr_command[0] == "Required":
        index = int(curr_command[-1])
        if 0 <= index < len(gifts):
            gifts[index] = cur_gift
    elif curr_command[0] == "JustInCase":
        gifts[-1] = cur_gift
    command = input()
for gift in gifts:
    if gift != "None":
        print(gift, end=" ")