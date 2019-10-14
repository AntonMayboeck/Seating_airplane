#1. Get an input a number
#2. See if its larger than 0 and if its move to step 3 if not step 6
#3. Get an second input and subtract with the first number 
#4. If the oucome is larger than zero assign that number max_int
#5. If not assign the first number max_int
#6. Halt if a number is smaller than zero

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
# Fill in the missing code
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    print(max_int)
print("The maximum is", max_int)    # Do not change this line
