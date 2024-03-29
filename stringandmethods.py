name='Anisha'
print(name[0])
print(name[-2])
name="Anisha" + "it"
print(name)


#string slicing
#stringname[start argument:stop argument:step argument]
print("harshit vashishta"[1:5])
print("harshit vashishta"[1:10:2])
print("harshit vashishta"[8:1:-1])
print("harshit vashishta"[::-1])

#print name in reverse order
# name2=input("enter your name")
# print(name2[::-1])

#string methods

print(len(name)) #returns the length of string 
print(name.lower( )) #converts all characters in string to lower case
print(name.upper()) #converts all characters in string to uppercase
print(name.title()) #capitalizes first letter of each word in a string
print(name.count("a"))  #returns the number of non-overlapping occurrences of substring in string
print(name.lower( ).count("a")) #returns the number of lowercase 'a' in string
print(name.replace("a","A"))  #replaces all occurances of substring with another substring
print(name.find("i"))    # returns the lowest index in the string where substring is found, else -1
print(name.find("i",5))    #search for "i" starting from index 5
print(name.center(10,"*"))    #Returns a centered string, surrounded by specified fill character (default is space)


namee="              anisha                  "
print(namee.strip())   #removes leading and trailing whitespaces
print(namee.lstrip( ) ) #removes only leading whitespaces
print(namee.rstrip() ) #removes only trailing whitespaces

# string are immutable
# stringg="anisha"
# stringg[2]=A  this will give error because strings are immutable we cannot change value