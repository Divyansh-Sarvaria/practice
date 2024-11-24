# error handling OR exception handling
# control over the error in program

# error in program
# 1
# _______
# print(x)
# _______
# -- solution --  
try:
  print(x)
except NameError:
  print("x is not defined")  

# 2 
x="python"
y=5

try:
  c=x+y
  print(c)
except TypeError:
  print("cant add string with integer")

# 3
name = "xyz"

try:
  er = int(name)
  print(er)
except ValueError: 
  print("cant be converted")
# 4
Name = ["x","y","z"]
try :
  print(Name[4])
except IndexError:
  print("wrong index")


