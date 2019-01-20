
sales = float(input("Enter sales: $"))

while sales >=0 :
    if sales > 1000:
        bonus = 15.0/100 * 1000
    else:
        bonus = 10.0 / 100 * 1000

    print("bonus= ",bonus)
    sales = float(input("Enter sales: $"))