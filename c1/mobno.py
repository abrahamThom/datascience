def find_absent_digits(mobile_number):
    all_digits = set('0123456789')
    mobile_digits = set(mobile_number)
    absent_digits = sorted(all_digits - mobile_digits)
    return absent_digits


mobile_number = input("Enter a 10-digit mobile number: ")
if len(mobile_number) == 10:
    absent_digits = find_absent_digits(mobile_number)
    if absent_digits:
        print(f"The absent digits in {mobile_number} are:", ', '.join(absent_digits))
    else:
        print(f"All digits from '0' to '9' are present in {mobile_number}.")
else:
    print("Invalid input! Please enter exactly 10 digits.")