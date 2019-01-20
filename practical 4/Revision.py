# count = 0
# counter=0
# total=0
# months = int(input("Enter number of months "))
# incomelist = []
# while count != months:
#     income = int(input("Enter income for month {} :".format(count+1)))
#     count += 1
#     incomelist.append(income)
#
# for i in incomelist:
#     counter+=1
#     total = total + i
#     print("Month {} - income: $ {:3} Total:$ {:2}".format(counter, i, total))

count=0
numbers=[]
while count<5:
    number = int(input("Enter number: "))
    count+=1
    numbers.append(number)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[4]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/count))