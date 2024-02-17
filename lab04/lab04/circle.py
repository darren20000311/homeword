import sys
import math

def circle(radius):
    #I use the  Pythagorean theorem to solve this problem.
    #First, we need to make sure the os have coverd from the left to the right include the center of the circle.
    # so we use the for loop to iterate -radius to radius+1. plus one is because we need to include the edge of the right circle
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            # in every iteration, we calculate the current a and b's position to the center of the circle.
            # therefore, distance= c**2. Because in the Pythagorean theorem a**2 + b**2 = c**2
            distance = math.sqrt(a**2 + b**2)
            # and then we need to compare the distance and the radius.
            #if distance<=radius+0.5 means this position is in the circle. Then, it will print out an o.
            if distance <= radius + 0.5:
                sys.stdout.write("o")
            #If not, it will print out a space.
            else:
                sys.stdout.write(" ")
        #Lastly, we need to change line, letting the picture to be a circle.
        sys.stdout.write("\n")
circle(20)
for j in range(6):
    print('1')