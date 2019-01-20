# score = float(input("Enter Score: "))
# if score <0 or score >100:
#     print("Invalid Score")
# elif score < 50:
#     print("Bad")
# elif score<90:
#     print("Passable")
# else:
#     print("Excellent")


# for i in range(20,0,-1):
#     print(i,end=" ")
# print()

num = int(input("Enter number of items "))
count = 0
total = 0
while count < num:
    count = count+ 1
    item = int(input("enter price of item "))
    total = total + item
print("Total price for ", count , " items is $",total)