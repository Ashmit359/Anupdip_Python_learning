# #1 write a program to find out the greatest number among four number 
# # take input form user 
# num1 = int (input("enter your first number : "))
# num2 = int (input("enter your second number : "))
# num3 = int (input("enter your third number : "))
# num4 = int (input("enter your four number : "))
# # check greatest number 
# if   (num1 == num2 and num1 == num3 and num1 == num4):
#     print("all number are equal ")
# elif (num1 >= num2 and num1 >= num3 and num1 >= num4):
#     print(num1, "num1 is greatest number ")
# elif (num2 >= num1 and num2 >= num3 and num2 >= num4):
#     print(num2, "num2 is greatest number ")
# elif (num3 >= num1 and num3 >= num2 and num3 >= num4):
#     print(num3, "num3 is greatest number ") 
# else:
#     print(num4, "num4 is greastest number "),
  


# #2 write a program to input any three number and arrange them in ascending order
# # take input from user 
# num1 = int (input("enter first number : "))
# num2 = int (input("enter second number : "))
# num3 = int (input("enter third number : "))
# # check greatest and smallest number 
# if(num1 == num2 and num1 == num3):
#     print("all numbers are equal ")
# elif(num1 <= num2 and num1 <= num3):
#     print("ascending order :- ", num1,num2,num3)
# elif(num2 <= num1 and num2 <= num3):
#     print("ascending order :- ", num2, num1, num3)
# else:
#     print("ascendig order :- ", num3, num1, num2),



# #3 while loop 
# x = 10 
# while (x <= 30):
#     print(x)
#     x = x + 6,


# #4 while loop 
# m = 10
# while(m <= 40):
#     print(m,end=",")
#     m=m+2

# # print the following sequence
# # 5,9,13,17,21........,205,209

# term = 5
# while(term <= 209):
#     print(term, end=",")
#     term = term + 4


# take percentage input from user and base on  percentage value you have to print 
# that student is in distinction (Percentage>70) /first class(Percentage>60)/
# sencond class (percentage >50)/third class (percentage >35)/fail(percentage is less than 35)

# Taking percentage input from the user
marks = int(input("Enter your percentage: "))

# Checking the conditions to determine the class
if marks > 70:
    print("Student passed with distinction.")
elif marks > 60 and marks <= 70:
    print("Student passed with first class.")
elif marks > 50 and marks <= 60:
    print("Student passed with second class.")
elif marks > 35 and marks <= 50:
    print("Student passed with third class.")
else:
    print("Student failed.")
