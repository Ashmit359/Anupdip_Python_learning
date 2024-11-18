# write a program to find out the greatest number among four number 
# take input form user 
num1 = int (input("enter your first number : "))
num2 = int (input("enter your second number : "))
num3 = int (input("enter your third number : "))
num4 = int (input("enter your four number : "))

# check greatest number 
if   (num1 == num2 and num1 == num3 and num1 == num4):
    print("all number are equal ")
elif (num1 >= num2 and num1 >= num3 and num1 >= num4):
    print(num1, "num1 is greatest number ")
elif (num2 >= num1 and num2 >= num3 and num2 >= num4):
    print(num2, "num2 is greatest number ")
elif (num3 >= num1 and num3 >= num2 and num3 >= num4):
    print(num3, "num3 is greatest number ") 
else:
    print(num4, "num4 is greastest number "),
  


# write a program to input any three number and arrange them in ascending order
# take input from user 
num1 = int (input("enter first number : "))
num2 = int (input("enter second number : "))
num3 = int (input("enter third number : "))

# check greatest and smallest number 
if(num1 == num2 and num1 == num3):
    print("all numbers are equal ")
elif(num1 <= num2 and num1 <= num3):
    print("ascending order :- ", num1,num2,num3)
elif(num2 <= num1 and num2 <= num3):
    print("ascending order :- ", num2, num1, num3)
else:
    print("ascendig order :- ", num3, num1, num2)           