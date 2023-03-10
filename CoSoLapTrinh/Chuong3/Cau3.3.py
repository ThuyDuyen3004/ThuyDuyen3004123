a=float(input('Tieu thu='))
if a<=100:
    t=550*a 
    VAT=0.1*t
    n=t+VAT
if a>100:
    t=550*100+750*(a-100) 
    VAT=0.1*t
    n=t+VAT
if a>150:
    t=100*550+750*50+(a-150)*950
    VAT=0.1*t
    n=t+VAT
if a>200:
    t=100*550+750*50+950*50+1350*(a-200)
    VAT=0.1*t
    n=t+VAT
print('Phai tra=',n)
    
      
