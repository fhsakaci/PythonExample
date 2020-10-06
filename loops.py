isimler = ["zeyneb","eda","melisa"]

for isim in isimler:
    print(isim)

for sayi in range(1,10,2):# 1 ile 10 arasında 2şer 2şer artar 
    print(sayi)

sayac=1
while sayac<=5:
    print(sayac)
    sayac= sayac + 1

isim = input("Adınız :")
print("isiminiz : " + isim)

faktoriyel = 1
sayi1 = int(input("faktöriyeli hesaplanacak sayıyı giriniz : "))
if sayi<0:
    print("negatif sayıların faktöriyeli olmaz.")

elif sayi1==0:
    print("0'ın faktöriyeli 1 dir.")
else:
    for i in range(1,sayi1 + 1):
      faktoriyel = faktoriyel * i  
    
print(str(sayi1) ,"sayısının faktöriyeli: ", faktoriyel)
