string = input().split()

s = []
for i in range(len(string)):
    s.append(int(string[i]) * -1)

print(s)
