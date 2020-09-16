
print("x")
x = int(input())
print("y")
y = int(input())
print("z")
z = int(input())


c=1
i=0
l=list()
while (c==1):
  if (y >=2):
      temp=int(y/2)
      m=int(y%2)
      i+=1
      y=temp
      l.append(m)
  else:
      temp = int(y / 2)
      m = int(y % 2)
      l.append(m)
      c=0
print (l)

temp=1
l.reverse()
for i in range (len(l)):
    if (l[i]==1):
      t=temp
      print(temp * temp * x, "mod", z)
      temp= temp*temp *x % z
      print( l[i], temp )
      d=0
    else:
        t=temp
        print(temp * temp, "mod", z)
        temp= temp*temp %z

        print(l[i], temp)
        d=1
if (d==0):
    print ("res=",temp)
else:
    print ("res=",temp )
