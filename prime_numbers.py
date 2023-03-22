def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

max_num = int(input("Enter a number: "))

for num in range(2, max_num + 1):
    if is_prime(num):
        print(num)
