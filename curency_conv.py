a=int(input("enter 1 to convert dollar into Indian Rupee \n2 to convert Indian Rupee into dollar: "))
if a == 2:
  doller=int(input("enter the ammount: "))
  float(doller)
  inr = doller*84.03
  print(inr)
elif a == 1:
  inr=int(input("enter the ammount to convert: "))
  float(inr)
  doller=inr*0.012
  print(doller)
else:
  print("wrong chooice")


