def char_in_range(a, b):
    return [chr(c) for c in range(ord(a) + 1, ord(b))]


ch1 = input()
ch2 = input()

res = char_in_range(ch1, ch2)

print(' '.join(res))
