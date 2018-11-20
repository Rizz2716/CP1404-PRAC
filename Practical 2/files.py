temp_file= open("temp","r")
firstchr=temp_file.read(2)
print(firstchr)
first_line_st=temp_file.readline()
print(first_line_st)

for line_str in temp_file:
    print(line_str)
temp_file.close()
