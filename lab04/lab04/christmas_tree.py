size = int(input("Please enter the size: "))
#Because we can only input odd number, we use this methd the check whether the number that the user
#input is odd number or not.
if size % 2 != 1:
    print("Please enter an odd number! ")
#This line we create the top of the *.
#the reason why size need to //2 is because I found the pattern that the number of space is the size of tree//2.
top = ' ' * (size//2) + '*'
#The reason why size = size//2 is because if the user input 5, we only need 5 lines ,including
# 2/ on the left and 2\ on the right, and _ at the botton.
size = size // 2
print(top)
#From this line, we started to iterate.
for i in range(size):
    # This line will appear the botton line. Because the boton we don't want the space.
    if i == size-1:
        print("/"+(2*i+1)*"_"+"\\")
    # And this line, I also found the pattern that the left of the number will decrease, and the right will increase.
    #And then it will show the appropriate figure.
    else:
        print(' '*(size-i-1)+'/'+(' '*(2*i+1))+'\\')
        