x=float(input("x="))
y=float(input("y="))
ch=str(input("Phep toan:"))
if (ch=="+" or ch=="-" or ch=="*" or ch=="/") and(y!=0):
     t=x+y
     print(str(x)+str(ch)+str(y)+"="+str(t))
else:
     print("Khong hop le")