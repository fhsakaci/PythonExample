sayi1=50
sayi2=7
sayi3=100

if sayi1>sayi2 and sayi1>sayi3:
    print("en büyük sayı : " + str(sayi1))
elif sayi2>sayi1 and sayi2>sayi3:
    print("en büyük sayı : " + str(sayi2))
elif sayi3>sayi1 and sayi3>sayi2:
    print("en büyük sayı : " + str(sayi3))

else:
    print("büyük sayı bulunamadı")    

if sayi1<sayi2 and sayi1<sayi3:
    print("en küçük sayı : " + str(sayi1))
elif sayi2<sayi1 and sayi2<sayi3:
    print("en küçük sayı : " + str(sayi2))
elif sayi3<sayi1 and sayi3<sayi2:
    print("en küçük sayı : " + str(sayi3))

else:
    print("küçük sayı bulunamadı")    
    
if sayi2<sayi1<sayi3   or sayi3<sayi1<sayi2:
    print("ortanca sayı : " + str(sayi1))  
elif sayi1<sayi2<sayi3   or sayi3<sayi2<sayi1:
    print("ortanca sayı : " + str(sayi2))  
elif sayi1<sayi3<sayi2   or sayi2<sayi3<sayi1:
    print("ortanca sayı : " + str(sayi3))  
else:
    print("ortanca sayı bulunamadı")    

 