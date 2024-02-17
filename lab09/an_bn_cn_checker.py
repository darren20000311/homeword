from an_bn_cn import AnBnCn as AnBnCn


def main():
    an_bn_cn = AnBnCn()
    line = input("Input a string:\n")
    if an_bn_cn.accept(line):
        print("This string is accepted")
    else:
        print("This string is rejected")


main()