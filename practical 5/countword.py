# import re
# line = " I am having a very nice day."
# count = len(re.findall(r'\w+', line))
# print (count)

# words=input("Enter a string: ")
# for word in words:
#     print(word,len(word))

words=input("Enter a string: ")
counts = dict()
words = str.split(words)
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for key, value in counts.items():
    print(("{} : {}".format(key,value)))
