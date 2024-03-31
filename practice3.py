#function that returns dictionary containing cube of numbers
def cube_finder(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i]=i**3
    return cubes

num=int(input("enter num:"))
print(cube_finder(num))

