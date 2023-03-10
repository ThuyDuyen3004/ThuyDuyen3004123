M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S=int(input("S="))
if S<= 100:
    t=S*M1
if S>=101 and S<=150:
    t=(S-100)*M2+100*M1
else:
    t=(S-150)*M3+M2*50+M1*100
    print("Phai tra=",t)