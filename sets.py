s={1,2,3,3,5}
print(s)

s.add(4)
s.remove(3)
s.discard(2)
s.clear()
print(s)

s1={1,2,3,6}
s2={1,4,7,3}
print("Union: ",s1|s2)          # Union 
print("Intersection: ", s1&s2)   # Intersection

#SET COMPREHENSION
s1={k**2 for k in range(1,11)}
print(s1)