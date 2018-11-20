# items = input(float("Enter number of items: "))
#
# while items >0:
#     total_price = input(float("Enter price of item"))
#     while items < 0:
#         items = items-1
#         total_price = total_price + total_price
#
# print(total_price)

num=int(input("Enter number of items "))
while (num<=0):
    print("enter positive number")
    num = int(input("enter number of items "))
total=0.0
for i in range (0, num):
    price=float(input("Enter price of item "))
    total+=price
    print("price", price, "total= ", total)

if total >100:
    total= 0.9*total
    print("Total price of items is ", total)
