names=['abc','abcd','abcde']
pos=0
for name in names:
    print(f"{pos}--->{name}")
    pos+=1

for pos,name in enumerate(names):
    print(f"{pos}--->{name}")