user_info={'name':'anisha', 'age':20, 'city':'New York'}
print(user_info)
print(type(user_info))

for i in user_info:        
    print(i)

for m in user_info.keys():
    print(m)

for j in user_info:
    print(user_info[j])

for k in user_info.values():
    print(k)

for l,n in user_info.items():
    print(n)
    print(l)

d=dict.fromkeys(('country','phone'),None)
print(d)

e=dict.fromkeys('abc',None)
print(e)

e.clear()
print(e)