def digit_count(string):
    counter = 0
    for ch in string:
        if ch.isdigit():
            counter += 1
    return True if counter >= 2 else False


def validator(string):
    is_valid = True
    if len(string) < 6 or len(string) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not string.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    if not digit_count(string):
        is_valid = False
        print("Password must have at least 2 digits")
    return is_valid


password = input()

if validator(password):
    print("Password is valid")
