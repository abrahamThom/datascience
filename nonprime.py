start = int(input("Enter the start value : "))
limit = int(input("Enter the limit value : "))

non_prime = []
flag = 0

for x in range(start,limit+1):
    half = int(x/2)
    for i in range(2, half+1):
        if x % i == 0:
            flag = 1

    if flag == 1:
        non_prime.append(x)

    flag = 0

print("Non-Prime numbers are ", non_prime)