import itertools


def getNumber():
    NUMBER1 = input('Enter the first number: ')
    NUMBER2 = input('Enter the second number: ')
    return NUMBER1, NUMBER2


def countCarries(NUMBER1, NUMBER2):
    carry = 0
    answer = 0
    #Since the length of number may be vary, so I use this function that allow the program
    # can calculate any length of the number.
    #[::-1] means that we want to calculate the right most number first.
    # and fillvalue = 0 is because when the two numbers length are different
    # one can add 0 at the front, so that they can calculate.
    for first_num, second_num in itertools.zip_longest(NUMBER1[::-1], NUMBER2[::-1], fillvalue='0'):
        carry = int(((int(first_num) + int(second_num) + carry) // 10))
        answer += carry
    return answer


def main():
    NUMBER1, NUMBER2 = getNumber()
    result = countCarries(NUMBER1, NUMBER2)
    print(result)


main()
