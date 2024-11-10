age = 17 

if(age>=18):
    print("You are eligible to vote")
else:
    print("you are not aligible to vote")

light1 = "green"


if(light1 == "yellow" ):
    print("please start your car") # this space called indentation
elif(light1=="red" or light1=="green"):
    print("go")
else:
    print("please wait")  

#Example
marks = int(input("Enter The Marks:"))
if(marks>= 90):
    Grade = "A"
elif(90>marks and marks>=80):
    Grade = "B"
elif(80>marks and marks >= 70):
    Grade = "C"
else:
    Grade = "D"   # this is called nested if else statement

print("Student Grade is is ->:", Grade)