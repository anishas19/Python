num=[1,6,4,23,12,5,3,2]
num.sort()
print(num)

print(sorted(num))

print(num.count(6))

num_copy=num.copy()
print(num_copy)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for sublist in matrix:
    print(sublist)  
    # for i in sublist: 
    #     print(i)
    
numbers=list(range(1,11))     #generate list in range
print(numbers)
numbers.pop()                 #changes original list 
print(numbers)

#index method
print(numbers.index(3))
print(numbers.index(3,1))

#pass list to a function
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(range(numbers)))