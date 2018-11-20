count=0
total=0.0
age = int(input("Enter age: "))
while age >=0:
    count+=1
    total+=age
    age=int(input("Enter age: "))
avg_age=total/count
print("The average age: ",avg_age)