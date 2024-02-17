symbol = input("Please enter the symbol: ")
width = int(input("Please enter the width: "))
height = int(input("Please enter the height: "))

for i in range(height):
    #In this line, i == 0 is because we want the first line of rectangle to be all symbol without any space.
    # and then height-1 is because we want the last line of rectangle to be all symbol without any space.
    if i == 0 or i == height-1:
        print(symbol * width)
    # In this line, width-2 is because we only want the middle of the rectangle to be empty.
    # and the first and the lasy to be all symbol.
    else:
        print(symbol + ' ' * (width - 2) + symbol)