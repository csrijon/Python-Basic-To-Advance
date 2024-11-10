# print("hello srijon", "hello monalish" )

# number = 78
# name= "srijon"
# age = 90.0

# print(number)
# print(name)
# print(age)

# print("my name is",name)
# print(type(name))
# print(type(age))

# sum of two number 
letter1 = 6 
letter2 = 9
print(letter1+letter2)

# logical operators 
print(not False)
print(not True)

# type conversion 
a = "4"
b =6.25
 #automatic type convert

# type casting  
a = int("4")
print(a+b)

#how to get input from user
name= input("enter your name:")
print("your name is:", name)

# pratice question 
# write a program to input 2 numbers & print their sum 
num1 = int(input("Enter The Number:"))
num2 = int(input("enter the secend number"))

sum = num1+num2
print("sumof two number:", sum)

#wap to input side of a square & print its area

side = int(input("enter the side of square:"))

area = side*side
print("area of square:", area)

# lets check folat value 
side1 = float(input("enter the side:"))

area1 = side1**side1
print("area of square:", area1)

#wap to input 2 floating point numbers & print their average

floatnum1 = float(input("Enter the 1st float number:"))
floatnum2 = float(input("Enter the secend number of float:"))

avg = (floatnum1+floatnum2) /2
print(avg)

#wap to input 2 int numbers a and bto b . print true if a is graterthan or eual to b if not print false
var = int(input("Enter the first number:"))
let = int(input("Enter the second number:"))
if var>=let:
    print("True")
else:
    print("False")