#1 write a program to calculate volume of sphere
radius = int (input("enter radius of volume : "))
pie = 3.14
volume = (4/3)*pie*(radius*radius*radius)
print ("volume of sphere is : " , volume)


#2 write a program to input cost price of book .then apply 20% discount on it. calculate the price to be paid by user
price = int(input("enter the cost price of book : "))
discount = price*(20/100)
print ("after discount user paid rs : ", (price - discount ))


#3 write a program to check a number is natural number or not
num = int (input("enter the any number "))
if (num>0):
    print(num, "the number is natural ")
else:
    print(num, "the number is not natural number ")    


#4 write a program to input marked price of a product. also input quantity. if the quantity is greater then 10 then apply a 
# discount of 20% otherwise apply 10% discount . then calculate the price to paid by customer #
marked_price = int(input("enter marked price of a product : "))
quantity = int (input ("enter quantity of product : "))
# initailize the discount
discount = 0
# calculating discount as per given criteria
if(quantity > 10):
    # discount of 20%
    discount = (marked_price*quantity*20)/100
else:
    # discount of 10%
    discount = (marked_price*quantity*10)/100
# calculate price to be paid by customer 
price = (marked_price*quantity)-discount    

# displying the data to user 
print("Marked price : Rs ", marked_price, "per unit")
print("quantity : ", quantity)
print("discount : ", discount)
print ("Total price Rs : ", marked_price*quantity)
print("Total price paid by user after discount : " ,price)


# write a program to input three angles and check they form a triangle or not 
# input of angles through keyboard
angle1 = float(input("enter first angles : "))
angle2 = float(input("enter second angles : "))
angle3 = float(input("enter third angle : "))

# displaying angles to the user 
print("first angle :", angle1)
print("second angle : ", angle2)
print("third angle : ", angle3)

# verifying triangle formation 
if((angle1 + angle2) > angle3) and ((angle1 + angle3) > angle3) and ((angle2 + angle3) > angle1):
    print("these angles form a triangle ")
else:
    print("these angles do not form triangle")    


# write a program to input three angles and check they form a triangle or not . 
# if they form a triangle then specify the type of triangle
# input of angles through keyboard
angle1 = float(input("enter first angles : "))
angle2 = float(input("enter second angles : "))
angle3 = float(input("enter third angle : "))

# displaying angles to the user 
print("first angle :", angle1)
print("second angle : ", angle2)
print("third angle : ", angle3)

# verifying triangle formation 
if((angle1 + angle2) > angle3) and ((angle1 + angle3) > angle3) and ((angle2 + angle3) > angle1):
    # acute angle triangle
    if(angle1 < 90 and angle2 < 90 and angle3 <90):
        print("above angles form an acute angled triangle ")
    else:
        if(angle1 == 90 or angle2 == 90 or angle3 == 90):
            print(" above angles form an right angled triangle ")
        else:
            print(" above angles form an obtuse angled triangle ")
else:
    print("these angle do not form triangle")