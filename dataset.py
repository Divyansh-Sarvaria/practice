# list in python 
# list store multiple data 
lis=['pavan','ivan','depanshu']
# touple can have multiple data 
Mytouple = ('pavan','ivan','depanshu')
# set store multiiple data
Myset = {'pavan',"ivan",'deepanshu'}
# dictionary store multiple data in key value pair
Dict = {"name":"pavan","email":"xyz@gmail.com"}
print("list : ", type(lis),"touple : ", type(Mytouple))
print("set :",type(Myset),"dictionary",type(Dict))
#  how to identify each :: 
# list -> []
# tople -> ()
# set ->{}
# dictionary -> { key : value }
# example of data set 
print("list : ",lis[0])
print("touple :",Mytouple[0]," : dictonary :" ,Dict["name"])
# acces complete data from a data set 
for data in lis:
  print("list :",data)
for item in Myset:
  print("set :",item)
for value in Mytouple:
  print("touple :",value)
for x in Dict.values():
  print("dictionary :",x)
# touple and set is unmutable :: Dictionary and list is mutable  
# to remove an element
Dict.pop("name")
Myset.remove("pavan")
lis.pop(0)
print("list : ",lis , "Set :" ,Myset,"Dictionary :",Dict)