
print("x")
x = int(input())
print("y")
y = int(input())
c=1
count=0
listx= list()
listy= list()
y5=y

print("x    " , "y    " , "phl" )
while (c!=0):
    if (x < y):
        print(x,"   " , y,"   " , "-" )
        listx.append(x)
        listy.append(y)
        t=y
        y=x
        x=t
    else:
        print(x,"   " , y,"   " , int(x/y) )
        listx.append(x)
        listy.append(y)
        c=x%y
        x=y
        y=c
    count+=1
print(x,"   " , y,"   " , "-" )
gcd=x
x1=1
y1=0
print("\n" )
print("x1" ,"    " , "y1" )
while (count!=0):
  #gcd = x*x1 + y*y1
  print (x1,"   ", y1 )
  count -= 1
  t=y1
  x1 = t
  y1 = int((gcd -listx[count]*x1 )/ listy[count])
print (x1,"   ", y1,"   " )

if (x1>0):
    print ("\n result = ",int(x1*1/gcd)%y5)
else:
    print("\n result = ", (int(x1 * 1 / gcd) + y5))

