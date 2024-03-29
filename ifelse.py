age=int(input("enter your age:"))
if age <=10:
    print("u r child")
elif age>10 and age<=18:
    print("u r teen")   
elif age>18 and age<=25:
    print("u r responsible now")
elif age>25 and  age<=60:
    print("working age")
else:
    print("u r lold")


name=input("enter your name")
if "s" in name:
    print("yes s is there in the string")
else:
    print("not present")

namee="sona"
if namee:
    print(f"hello {namee}")