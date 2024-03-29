number=1
name="anisha"
print(name)
print(number)

print(name +" always secure roll no "+ str(number))   #ugly syntax

#correct way
print("{} always secure roll no {}" .format (name,number)) #python3
print(f"{name} always secure roll no {number}")            #python3.6

#input from user
name2=input("enter ur name")
print(name+" and " +name2+ " both are good")

name3,name4="sakshi","pooja"
print(name + name2+  " and "+name3+name4)                     #concatenation of strings 

full_name,age=input("enter your name and age").split(",")       #splitting string into list
print(f"your name is {full_name} and your age is {age}")

