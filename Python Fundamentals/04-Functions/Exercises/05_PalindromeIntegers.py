def palindrome(seq):
    return True if seq == seq[::-1] else False


numbers = input().split(', ')
result = [palindrome(b) for b in numbers]


for i in result:
    print(i)

