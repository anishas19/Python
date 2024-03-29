# def sum(a,b):
#     return a+b
# print(sum(3,4))

def greater(a,b):
    if a>b:
       return a
    else:
        return b

def greatest(a,b,c):
    return greater(greater(a,b),c)

print(greatest(2,8,5))