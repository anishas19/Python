user_id=('user1','user2','user3','user4')
names=('ani','shob','adi','preet')

user_info=zip(user_id,names)
print("user info:",user_info)

#unpacking with * operator
l1,l2=list(zip(*user_info))
print(l1)
print(l2)

