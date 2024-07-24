def is_perfect_number(num):
    if num <= 0:
        return False

    sum_of_factors = sum(i for i in range(1, num) if num % i == 0)

    return sum_of_factors == num


def get_number():
    num = int(input("Enter a positive integer to check if it's a perfect number: "))
    return num


def main():
    num = get_number()
    if is_perfect_number(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")


if __name__ == "__main__":
    main()
