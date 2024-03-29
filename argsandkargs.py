def all_total(*args):
    total=0
    for num in args:
        total+=num
    return total

numbers=[1,2,3]
print(all_total(*numbers))

