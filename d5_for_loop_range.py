# # print the following sequence
# # 4,-8,12,-16,20,-24,..........,-816,820
# term = 4
# while(term <= 820):
#     if (term % 8 == 0):
#         print(- term, end=",")
#     else:
#         print(term,end=",")
#     term = term + 4        


# # FOR LOOP

# # exm-1
# for x in [80,70,20,50,620]:
#     print(x,end=",")

# # exm-2
# for m in [4,8,5,6,2]:
#     print((m**2), end=",")

# # exm -3
# sum = 0
# for x in [40,50,60,70]:
#     print(x ,end = ",")
#     sum = sum + x
# print("in sum", sum)    


# RANGE

#1 write a program to print first 20 natural number
# print ("first 20 natural number : ")
# for x in range (1,21):
#     print(x,end=" , ")

# write a program to print first 30 even natural number .also print their sum
sum = 0
for x in range (1,31):
    if(x % 2 == 0 ):
        print("first even natural number ", x)
        sum = sum + (x * 2)
print("in sum = ", sum)        