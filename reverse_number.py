a=int(input("enter the number"))
b=0
c=0
while(a!=0):
  b=a%10
  c=c*10+b
  a=int(a/10)
print(c)
