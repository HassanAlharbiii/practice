from datetime import datetime
user=input('Enter the names and Birth days (name:dd-mm-yyyy,name2:dd-mm-yyyy:...) :')
today=datetime.now()
users=user.split(',')
for user in users:

  x=user.split(':')
  name=x[0]
  date=x[1]
  print(date)
  print(name,end=" ")
  dateTimeObj = datetime.strptime(date, "%d-%m-%Y")

  print(f'{int((today-dateTimeObj).days/365)} years old',end=" ")

  weekday=dateTimeObj.weekday()
  if weekday ==0:
    print("She/He was born on monday")
  elif weekday ==1:
    print("She/He was born on tuesday")
  elif weekday ==2:
    print("She/He was born on  wednesday ")
  elif weekday ==3:
    print("She/He was born on Thursday")
  elif weekday ==4:
    print("She/He was born on Friday")
  elif weekday ==5:
    print("She/He was born on  Saturday ")
  elif weekday ==6:
    print("She/He was born on Sunday")