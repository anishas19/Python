num=(1,2,3,4,5)
print(num)
print(type(num))

number=tuple(range(1,11))   #create tuple
print(number)

fruits="apple","banana","litchi"
print(type(fruits))

f1,f2,f3=fruits
print(f1)
print(f2)
print(f3)

#tuple methods
fav=("name",19,['cat','dog'],['holy','gaya'])
fav[2].pop()
fav[2].append('fish')
print(fav)

#function
def sum_num(a,b):
    add=a+b
    mul=a*b
    return add, mul

addi,muli=sum_num(5,6)
print(addi)
print(muli)