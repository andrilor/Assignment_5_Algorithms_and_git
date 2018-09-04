#take a number
#make int for 4 numbers 
#int1, int2, int3, intX
#for i repet unt til number
#make exepsons for ver the number is 1,2, 3 and set the valu as 1,2,3
#then make the intX as int1+in2+int3
n = int(input("Enter the length of the sequence: ")) # Do not change this line
int1 = 0
int2 = 0
int3 = 0 
intX = 0
for i in range(1,n+1):
    if i == 1:
        int1 = i
        print(int1)
    elif i == 2:
        int2 = i
        print(int2)
    elif i == 3:
        int3 = i
        print(int3)
    else:
        intX = int1 + int2 + int3
        print(intX)
        int1 = int2
        int2 = int3
        int3 = intX