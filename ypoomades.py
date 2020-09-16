
print("x")
x = int(input())
l=list()
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd (b,a%b)

for i in range (1,x):
    if gcd(i,x) == 1:
        l.append(i)

res=list()
for i in range (len(l)):
   c=0
   ti=l[i]
   l1=list()
   res.append(l1)
   while (c==0):
    if ((ti% x)==1):
        l1.append(ti)
        c=1
    else:
        l1.append(ti)
        ti = (l[i] *ti) % x

print ("omades * ->" ,l )
print("ypoomades * ->", res, "\n\n"  )


l=list()
res=list()
for i in range (1,x):
     l.append(i)
for i in range (len(l)):
   c=0
   ti=l[i]
   l1=list()
   res.append(l1)
   while (c==0):
    if ((ti% x)==0):
        l1.append(ti)
        c=1
    else:
        l1.append(ti)
        ti = (l[i] + ti) % x

print( "ypoomades + ->",res)