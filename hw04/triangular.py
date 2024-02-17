import sys
def main(height):
    #we start from 1 is because we don't want the first line to be whitespace.
    #height+1 is because if we input 5, we want have 5 lines of *. Therefore, we need to +1
    for row in range(1, height + 1):
        print('*' * row)


main(int(sys.argv[1]))