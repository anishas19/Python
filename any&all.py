num1=[1,2,3,4,5,6,7,8,9,10]
num2=[2,4,6,8,10]

#all
print(all(num%2==0 for num in num1))
print(all(num%2==0 for num in num2))

#any
print(any(num%2==0 for num in num1))
print(any(num%2==0 for num in num2))