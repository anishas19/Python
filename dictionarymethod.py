user_info={'name':'anisha', 'age':20, 'city':'New York'}
print(user_info)

#pop method
popped_item=user_info.pop('name')   #argument is necessary
print(user_info)
print(popped_item)
print(type(popped_item))

#popitem method
pop_item=user_info.popitem()     #remove random item
print(user_info)

#update method
more_info={
    'fav_tunes':['radha','krishna'],
    'fav_movies':['shiddat','ek villain'],
    'name':'shob',
    'age':12
}

user_info.update(more_info)
print(user_info)

#get method
# print(user_info['city'])    shows key error
print(user_info.get('city'))  #shows none

#copy method
user=user_info.copy()
print(user_info)
print(user)

user.popitem()
print(user_info)
print(user)

#fromkeys method
d=dict.fromkeys(('name','age','city'),'unknown')
print(d)

e=dict.fromkeys('abc','unknown')
print(e)

f=dict.fromkeys(range(1,11),'unknown')
print(f)


