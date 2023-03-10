i=1
while i<=9:
  j=1
  while j<18:
       if j<=8+i and j>= 10-i:
           print("*",end=" ")
       else:
           print(" ",end=" ")
       j=j+1
  i=i+1
  print("\n")
  