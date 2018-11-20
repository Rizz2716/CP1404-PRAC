""""input a name and print altnertive character"""""
def main():
    name=input("enter your name")
    get_name(name)


def get_name(name):
    while len(name) < 1:
        name = input("Enter longer name")


    print(name[::2])

main()
"""to do"""