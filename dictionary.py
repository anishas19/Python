user_info={'name':'anisha', 'age':20, 'city':'New York'}
print(user_info)
print(type(user_info))
print(user_info['name'])
# print(user_info['harshit'])    show keyerror

user={}                          #create empty dictionary
user['name']='shob'              #insert key value 
user['age']=21
print(user)

#two method to print key of dictionary
for i in user_info:              #first
    print(i)

for m in user_info.keys():       #second
    print(m)

#two method to print values of keys of dictionary
for j in user_info:               #first
    print(user_info[j])

for k in user_info.values():       #second
    print(k)

#method for print key and value
for l,n in user_info.items():
    print(n)
    print(l)

# method to clear dictionary
user_info.clear()
print(user_info)