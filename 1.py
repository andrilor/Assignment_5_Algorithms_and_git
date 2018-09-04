#take an number1
#while number is biger then 0
#   take a diffrent number2 and 
#   cheke whits is biger 
#   remember the biger number
#   taka in another number 
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0
while num_int >= 0:
    if max_int < num_int:
        max_int = num_int
    num_int = int(input("Input a number: "))    # Do not change this line
print("The maximum is", max_int)    # Do not change this line
