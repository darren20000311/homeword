def main():
    print("Please enter a magic number")
    #First, we need to create an empty list to sotre the numbers that the user input.
    square = [ ]
    #Since, we can only calculate 3 lines of numbers. We use the for loop in the range of 3.
    for i in range(3):
        number = input()
        # If the user enter less than or more than 3 numbers or enter letters, it will return "Please enter 3 integer numbers!" 
        if len(number) !=3 and not number.isdigit():
            print("Please enter 3 integer numbers!")
        # we transter the char number into the integeer and store in the list of square that we created before.
        rows = [int(char) for char in number]
        square.append(rows)
    # Because we only need to have a 3 by 3 columns and rows, we only need the size of 3. 
    SIZE = 3
    #We initialize each columns and rows and diagonal lines.
    col_sum=[0,0,0]
    row_sum=[0,0,0]
    dia_sum1=0
    dia_sum2=0
    # Stared to iterate each numbers we enter
    for col in range(SIZE):
        for row in range(SIZE):
            col_sum[col] += square[row][col]
            row_sum[row] += square[row][col]
        #The reason this line of code need to like this is because col == row =[0][0][1][1][2][2]
        #It will become a diagonal line.
            if col == row:
                dia_sum1 +=  square[row][col]
        #This line is also want to find the other diagonal line. For example, when colum and row
        #become [0][2],[1][1],[2][0], we can find the other diagonal line.
            if col + row == 2:
                dia_sum2 += square[row][col]
    is_magic = True
    #We sarted to check the values of variable that we added before.
    for check in col_sum:
        #If it is not equal, is_magic become False.
        if check != 15:
            is_magic = False
            break
    for check in row_sum:
        if check != 15:
            is_magic = False
            break
    #The reason why dia_sum1 and dia_sum2 don't need to use for loop is because we just checked
    #before, so we don't need to iterate again
    if dia_sum1 != 15 or dia_sum2 != 15:
        is_magic = False
    if is_magic:
        print('This is a magic number')
    else:
        print('This is not a magic number')
main()