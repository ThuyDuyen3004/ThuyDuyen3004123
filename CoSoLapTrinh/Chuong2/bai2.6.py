name=input('Ho ten:')
s = int(input('So ngay cong:'))
t =int( input('Don gia ngay cong:'))
p=float(input('He so phu cap: '))
z = int(input('Tam ung: '))
v=t*s*p
k=round(v,1)
l=k-z
o=round(l,1)
print('Nhan vien '+str(name)+","+" Co tien Luong="+str(k)+","+" Tam ung="+str(z)+" va Thuc linh="+str(o))