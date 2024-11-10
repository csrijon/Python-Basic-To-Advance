a = int(input("Enter The First Input Number:"))
b = int(input("Enter The Second Input Number:"))
c = int(input("Enter The Third Input Number:"))

if(a>b and a>c):
    print(a,"is the largest number")
elif(b>a and b>c):
    print(b,"is the largest Number")
elif(c>a and c>b):
    print(c,"is the largest number")
else:
    print("All numbers are equal")

#four number 

num1 = float(input("Enter THe First Number:"))
num2 = float(input("Enter the Secend NUmber:"))
num3 = float(input("Enter the Third Number:"))
num4 = float(input("Enter the Fourth Number:"))

if(num1>=num2 and num1>=num3 and num1>=num4):
    print(num1,"is the largest number")
elif(num2>=num1 and num2>=num3 and num2>= num4):
    print(num2,"is the largest number")
elif(num3>=num4 and num3>=num1 and num3>=num2):
    print(num3,"is the largest number")
else:
    print(num4,"is the largest number")  

#other option

d = max(num1,num2,num3,num4)
print(d)