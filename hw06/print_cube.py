def main():
    #Since we can only input even number. 
    #So if the user inter an odd number, this program will not run.
    #And then in  order to complete the cube, I took the whole cube apart.
    SIZE = int(input("Input cube size (multiple of 2):"))
    if SIZE % 2 != 0:
        exit()
    TOP_LINE(SIZE)
    TOP_BODY(SIZE)
    MIDDLE_LINE(SIZE)
    MIDDLE_BODY(SIZE)
    BOTTON_CONOR(SIZE)
    BOTTON_BODY(SIZE)
    BOTTON_LINE(SIZE)


TWO = 2
ONE = 1


def TOP_LINE(SIZE):
    for i in range(SIZE):
        print((SIZE // TWO - i) * " " + "+" + (SIZE * TWO) * "-" + "+")
        break


def TOP_BODY(SIZE):
    for i in range(SIZE // TWO):
        if i == 0:
            print((SIZE // TWO - i - ONE) * " " + "/" + (SIZE * TWO) * " " + "/" + "|")
        else:
            print((SIZE // TWO - i - ONE) * " " + "/" + (TWO * SIZE) * " " + "/" + i * " " + "|")


def MIDDLE_LINE(SIZE):
    print("+" + (TWO * SIZE) * "-" + "+" + (SIZE // TWO - ONE) * " " + "|") 


def MIDDLE_BODY(SIZE):
    for i in range((SIZE // TWO) - ONE):
        print("|" + ((TWO * SIZE) * " ") + "|" + (" " * (SIZE // TWO - ONE)) + "|")


def BOTTON_CONOR(SIZE):
    print("|" + (TWO * SIZE * " ") + "|" + (SIZE // TWO - ONE) * " " + "+")


def BOTTON_BODY(SIZE):
    for i in range(SIZE // TWO):
        print("|" + (TWO * SIZE * " ") + "|" + (SIZE // TWO - i - ONE) * " " + "/")


def BOTTON_LINE(SIZE):
    print("+" + (TWO * SIZE) * "-" + "+")


main()





