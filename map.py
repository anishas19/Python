numbers=[1,2,3,4,5]
def square(n):
    return n*n

squares=list(map(square,numbers))
print(squares)

square_list=map(lambda a : a**2,numbers)
print(list(square_list))