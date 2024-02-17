import sys


ONE = 1
TWO = 2

def nose_cone(height):
    for i in range(height):
        #Because if the number that the user enter is an odd number, we output the normal triangle as usual.
        if height % TWO == ONE:
            print((height - i) * ' ' + (TWO * i + ONE) * '*')
        else:
            #If the number that the user enter is an even number, the first line of triangle should be removed,
            #so I use continue to skip the first line if the user enter an even number.
            if i == 0:
                continue
            print((height - i) * ' ' + ((TWO * i+ONE)) * '*')


def fuselage(width, height, striped = False):
    for i in range(height):
        for j in range(width):
            #This line is to calculate the number of lines for each  _ and X if striped.
            #Because the line of '_' is always less than the line of 'X', we need to minus one.
            if striped and j < (width/TWO)-ONE:
                print('_' * width)
            else:
                print('X' * width)


def tail(height):
    #height divided by TWO is because the tail starts from the middle of the triangle
    #And height plus one is because we want the last index included.
    for i in range(int(height/TWO), height + ONE):
        print((height - i) * ' ' + (TWO * i + ONE) * '*')
    #This line will let the tail to have one more botton line.
    print('*' * (height * TWO + ONE))


def main():
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    striped = len(sys.argv) == 4
    nose_cone(int(width/TWO))
    fuselage(width, height, striped)
    tail(int(width/TWO))

    
if __name__ == '__main__':

    main()








