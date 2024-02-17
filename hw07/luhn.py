def main():
    # First, we need to reverse the number that the user enter.
    ACCOUNT_NUMBER = input("Please enter your account number: ")[::-1]
    # Check whether the input that the user enter is digit or not.
    if ACCOUNT_NUMBER.isdigit():
        luhn(ACCOUNT_NUMBER)
    else:
        print("Invalid input. Please enter a numeric account number.")


def luhn(ACCOUNT_NUMBER):
    # Transfer the string into integer.
    ACCOUNT_NUMBER = [int(x) for x in ACCOUNT_NUMBER]
    # Start with 1 and step by 2 is because 
    # we want to double up the even number in the ACCOUNT_NUMBER
    for i in range(1, len(ACCOUNT_NUMBER), 2):
        ACCOUNT_NUMBER[i] *= 2
# If the number is bigger than 9, we need to mod 10 and plus 1,
# because by this way we can let the number that bigger than 9 adds together.
        if ACCOUNT_NUMBER[i] > 9:
            ACCOUNT_NUMBER[i] = ACCOUNT_NUMBER[i] % 10 +1
    total = sum(ACCOUNT_NUMBER)
    if total % 10 == 0:
        print("This account number is valid.")
    else:
        print("This account number is not valid.")


main()
# After running the code above, and enter the account that the instruction ask me to test.
# The result are as below.
# Please enter your account number: 79927398713
# This account number is valid.
# Please enter your account number: 49927398716
# This account number is valid.
# Please enter your account number: 1234567812345670
# This account number is valid.
# Please enter your account number: 12345675
# This account number is not valid.
# Please enter your account number: 49927398717
# This account number is not valid.
# Please enter your account number: 1234567812345678
# This account number is not valid.