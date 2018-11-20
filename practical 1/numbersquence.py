num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print("The even numbers are:")
for i in range(num1, num2, 2):
    print(i+2, end='')
print()

print("The odd numbers are:")
for i in range(num1, num2, 2):
    print(i+2, end='')
print()

print("The squares are:")
for i in range(num1, num2, 2):
    print(i*i, end='')
print()
