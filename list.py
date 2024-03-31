numbers=[1,2,3,4]
print(numbers)

# check type of list
print(type(numbers))

# list indexing
print(numbers[2])

# method to add element in list
numbers.append(2.5)      #using append method
numbers.insert(2,9)      #using insert method
print(numbers)

mixed=[2,'ani','true']
print(mixed)
mixed[1]="two"
mixed[1:]="two"
mixed[1]="two","three"
print (mixed)
print(mixed[-1])

numbers.insert(1,mixed)
print(numbers)

numbers.pop()
del numbers[1]
print(numbers)

user_info=['anisha','20']
print(','.join(user_info))

fruits=['apple','banana','cherry']
for i in fruits:
    print(i)


#LIST COMPREHENSION

square=[i**2 for i in range(1,11)]
print(square)

names=['john','anisha','amita']
namefst=[name[0] for name in names]
print(namefst)

namervrse=[name[::-1] for name in names]
print(namervrse)

evn=[num for num in range(1,11) if num%2==0]
print(evn)

evn_odd=[num if (num%2==0) else (-num) for num in range(1,11)]
print(evn_odd)

example=[[i for i in range(1,6)] for j in range(1,6)]
print(example)