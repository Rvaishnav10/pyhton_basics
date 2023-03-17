att=int(input("enter the attendance in %"))
clss=int(input("enter clas:"))
s=input("enter medical status:")
if att>75:
  print("student is allowed")
elif att<75:
  if s=="submitted":
    print("student is allowed by permission ")
  else:
    print("student not allowed")
