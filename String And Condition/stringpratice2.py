str1  = "srijon"
print(len(str1))
print(str1[1])
print(str1[1:5]) 
print(str1[1:]) #[1:len(str1)]
print(str1[:5]) #[0:5]

print(str1[-3:len(str1)])

print(str1.endswith("on")) #return true if string end with sub string
print(str1.capitalize()) #captalizes 1st char
str2 = "my name is srijon chowdhury. and i am ceo of makaut"
print(str2.replace("srijon","javascript")) #replcae old word and new word in a string
print(str2.find("name"))
print(str2.count("a"))
