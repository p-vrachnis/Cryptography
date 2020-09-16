
print("x")
x = int(input())
c=1
i=0
l=list()
print("\nQuotient | Remainder | Bit \n" )
while (c==1):
  if (x >=2):
      temp=int(x/2)
      m=int(x%2)
      print(temp ," | ", m , " | ", i )
      i+=1
      x=temp
      l.append(m)
  else:
      temp = int(x / 2)
      m = int(x % 2)
      print(temp, " | ", m, " | ", i)
      l.append(m)
      c=0
l.reverse()
print("\n",l)
