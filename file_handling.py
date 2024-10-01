# crate file saying laptop pasward
# open function will creat the file when the file does not exist 
mypass = open("pasword.txt","w")
# write the laptop pass in the file
mypass.write("__qazxsw__ is the pasword to my pc ")
# adding a line or word using user Input
# a=input("enter the passward : ")
# mypass.write(a)
# read passward form file 
mypass= open("pasword.txt","r")
print(mypass.read())
 
mypass= open("pasword.txt","r")
mydata = mypass.read()
if "pasword" in mydata:
  print("yes") 
else:
  print("no")
 
mypass.close()
import os 
os.remove("pasword.txt")



# creating a csv file
myCsv = open("CsvFile.csv","w")
myCsv.write("this is a casv file")
# creating a exel file
MyExel = open("Myexel.xlsx","w")
MyExel.write("this is a exel file")
