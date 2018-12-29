# name = input("Enter your name: ")
# counter = 0
# vowel = "aeiou"
#
# for i in name:
#     if i.lower() in vowel:
#         counter += 1
#
# print("Out of {} letters, {} has {} vowels".format(len(name), name, counter))


# letters= list("things")
# letters = [ 't', 'h', 'i','n', 'g', 's']
# newstring= "things"
# print(newstring)
# print(newstring.upper())

# letters[0]='s'
# print(letters)
#
# print("hello"+newstring)
# print(letters[:3:])
# print(newstring[:3:])


# myList= [1,'a', 3.14334, True]
#
# print(myList[1])
# print(myList[:3])

things=['a',[1,2,3], 'z']
#
# for thing in things:
#     print(things, end='')
# things.append('z')
things.insert(1,'python')
print(things)
# things.remove('a')
# print(things)
#
# numbers=[1,3,2]
# numbers.sort()
# print(numbers)

# word=['hello', 'zoo', 'yankee']
# word.sort()
# print(word)
# word.reverse()
# print(word)

# from operator import itemgetter
# data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
# data.sort(key=itemgetter(1))
# print(data)

# words = '1. Heartbreak Hotel - Elvis Presley (1956)'.split()
# for i in range(len(words)):  # capitalise each word
#     words[i] = words[i].title()
# text = ' '.join(words)  # put commas between words
# print(text)

# scores = []
# score = int(input("Score: "))
# while score>=0:
#     scores.append(score)
#     score = int(input("Score: "))
# print("Your highest score is", max(scores))
# print(scores)
