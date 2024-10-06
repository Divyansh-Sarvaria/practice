from datetime import datetime
# creatina the current date and time var to pull out month yeart and date
def calcAge(BirthDate):
  rn = datetime.today()
  # getting total yeas lived
  y=rn.year-BirthDate.year
  # getting total days lived
  td= (rn - BirthDate).days
  # getting total months lived
  tm = (rn.year - BirthDate.year) * 12 + rn.month - BirthDate.month
  if rn.day < BirthDate.day:
    tm -= 1   
  return y , tm , td
Birthip = input("enter the birth date in dd-mm-yyyy format : ")
date = datetime.strptime(Birthip,"%d-%m-%Y")
y , tm , td =  calcAge(date)

print(f"Your age is: {y} years, {tm} months lived, and  {td} days lived.")