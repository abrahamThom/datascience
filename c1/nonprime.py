def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num * 0.5)+1, 2):
        if num % i == 0:
            return False
    return True
a=int(input("Enter starting number:"))
b=int(input("Enter ending number:"))
print("Non prime numbers from ",a," to ",b," are:")
for i in range(a,b+1):
    if not is_prime(i):
        print(i)
