#  LISTS 
# 1. list can store multiple data and data can  be of diffrent type 
# 2. list can store the duplicate data 
# 3. list is an ordered data set -- sorting accending or decending
# create list and store the name of a few people 
people = ["divyansh" , "harsh " , "jeet" , "sahil", "sumit "]

# ________________________________________________
# add a name in the list  
people.append("ayz")
people.append(34)
print(people) 
print("___________________________________________")
# ________________________________________________
# add a value using idex value 
people.insert(3,"faizal")
print(people) 
print("___________________________________________")
# ________________________________________________
# to acces data using index no 
print(people[1])
print("___________________________________________")
# ________________________________________________
# acces the complete list
print("___________________________________________")
a=len(people)
i=0
while i< a:
   print(people[i])
   i=i+1
print("___________________________________________")
# using while loop
for i in people:
  print(i)
print("___________________________________________")
# ________________________________________________
# deletion of an element
people.remove("divyansh")
print(people)
print("___________________________________________")
# deletion of specific index
people.pop(2)
print(people)
print("___________________________________________")

# practice work
# ----------------------------------
# add 5 fav city name in list
city  = ["delhi","goa","mumbai","kolkata","pune"]
print(city)
print("___________________________________________")
# add kasol at inddex 0
city.append(0,"kasol")
print(city)
print("___________________________________________")

# sorting the list data

# print the list data 
# ----------------------------------