def perfect(num):
    divisors = [d for d in range(1, num) if num % d == 0]
    sum_of_divisors = sum(divisors)
    return True if sum_of_divisors == num else False


number = int(input())

if perfect(number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")

