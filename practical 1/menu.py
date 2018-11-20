name=str(input("Enter your name: "))

print("(H)ello \n(G)oodbye \n(Q)uit")


option=input("Enter your choice ").upper()
while option!="Q":
    if option == "H":
        print("Hello",name)
    elif option == "G":
        print("Goodbye", name)
    else:
        print("invalid option")
    print("(H)ello \n(G)oodbye \n(Q)uit")
    option = input("Enter your choice ").upper()
print("finished")