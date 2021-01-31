year = int(input())
# year += 1
# while True:
#     if len(str(year)) == len(set(str(year))):
#         print(year)
#         break
#     year += 1

while True:
    is_happy = True
    string = str(year)
    for index_1 in range(len(string)):
        for index_2 in range(len(string)):
            if index_1 == index_2:
                continue
            if string[index_1] == string[index_2]:
                is_happy = False
                break

    if is_happy:
        print(year)
        break
    else:
        year += 1

