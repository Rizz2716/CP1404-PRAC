def main():
    """Display income report for incomes over a given number of months."""
    numbers = []
    num1 = 5
    print("Enter 5 numbers")
    for num1 in range(1, num1 + 1):
        number = int(input("Enter number " + str(num1) + ": "))
        numbers.append(number)
    print("The first number is", numbers[0])
    print("The last number is", numbers[4])
    print("The smallest number is", min(numbers))
    print("The biggest number is", max(numbers))
    print("The average of the numbers is", sum(numbers)/num1)
main()
