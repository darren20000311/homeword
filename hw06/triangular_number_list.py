def triangular_number(number):
    # i found out that we can use Gauss formula to calculate the number of * in each triangle
    # and the formula is n（1+n）/2.
    return ((1 + number) * number) // 2


def main():
    # creat an empty list to store the result.
    triangular_number_list = []
    while True:
        number = input("Enter a number, or enter 'done':")
        # follow the instruction, if the user enter done, the loop will break.
        if number == 'done':
            break
        else:
            number = int(number)
            result = triangular_number(number)
            #append the result in the empty list that we just created.
            triangular_number_list.append(result)
    print(triangular_number_list)


main()
