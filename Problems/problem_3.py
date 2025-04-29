3# This program will print a countdown from 10 to 1 for spaceship and then print "Liftoff!"
# using while loop
print("Spaceship launching program! \n coundown Start!")
def space_ship():
    i: int=10
    while(i>=1):
        print(i, end=" ")
        i= i-1
    print(" Liftoff!")
space_ship()
# using for loop
for i in range(10, 0, -1):
    print(i, end=" ")
print("  Liftoff!")