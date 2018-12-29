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
                    print("{0} {1:>5}".format(num + 1,learned + row[0]),"-",row[1] , "(" + row[2] + ")")
                    num += 1
                print("\n",countn,"songs learns", countr,"songs still to learn")
        elif option == "A":
            print("Add new song")
            # To do add the song to the file
            # output_file = open("songs.csv","w")
            #
            # print(newsong,file=output_file)
            # output_file.close()
            # temp_file = open("songs.csv", "a")
            # songslist = temp_file.readlines()
            # # print(songslist, file=temp_file)
        elif option == "C":
            print("complete a song")
            # To do edit y in the song to complete the song
            # song_num=input("Enter the number of the song to be marked as learned")
            # while song_num != num:
            #     num += 1
            #         if song_num = num
            #         parts = song.strip().split(",")
            #         part[4].replace("y","n")

        else:
            print("invalid option")
        print(MENU)
        option = input("Enter your choice ").upper()
    print("finished")

main()

# test_list = []
# test_list = songs_list
# for song in test_list:
#     num += 1
#     if num == song_num:
#         songs_list = []
#         print(song[-2])
#         song[-2].replace("y", "n")
#         print(song[-2])
#         songs_list.append(song)
#
#     else:
#         songs_list.append(song)
#
# while len(year) < 4 or len(year) > 4:
#     if year != int:
#         print("Invalid input, enter a valid number")
#     elif year < 0:
#         print("Number must be more than 0")
#     elif year > 4:
#         print("Invalid input")
#     elif year == str:
#         print("Invalid input, Enter numbers")
#     else:
#         print(year)
#     print("Input cannot be blank")
#     year = input("Enter year:\n")