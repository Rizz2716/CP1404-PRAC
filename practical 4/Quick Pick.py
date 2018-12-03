
def main():
    import random

    num=int(input("How many quick picks?: "))

    while num>0:
        number=(random.sample(range(1,45), 6))
        num-=1
        number.sort()
        number = ' '.join(str(a) for a in number)
        print(number)

main()