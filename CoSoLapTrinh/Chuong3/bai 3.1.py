import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
s=p*(p-a)*(p-b)*(p-c)
v=math.sqrt(s)
r=round(v,3)
if a+b>c and a+c>b and b+c>a:
    print("Dien tich=",r)
else:
    print("Khong hop le")
