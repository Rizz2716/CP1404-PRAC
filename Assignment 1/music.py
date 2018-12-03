import csv

def main():

    MENU = """ Menu:
        L - List songs
        A - Add new song
        C - Complete a song
        Q - Quit"""

    print("Welcome Rizwan")
    print(MENU)

    option=input("Enter your choice ").upper()
    while option!="Q":
        num = 0
        countn=0
        countr=0
        if option == "L":
            with open('songs.csv') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if row [3]=='y':
                        learned="* "
                        countr+=1
                    else:
                        learned="  "
                        countn+=1
                    print("{0} {1:>5}".format(num + 1,learned+ row[0]),"-",row[1], "("+row[2]+")")
                    num+=1
            print("\n",countn,"songs learns", countr,"songs still to learn")
        elif option == "A":
            print("Add new song")
        elif option == "C":
            print("complete a song")

        else:
            print("invalid option")
        print(MENU)
        option = input("Enter your choice ").upper()
    print("finished")

main()