

class Mat:
    def __init__(self,sayi1,sayi2): #constructer = yapıcı blok
        self.s1 = sayi1
        self.s2 = sayi2
        print("mat başladı(referans oluştu)")
    def topla(self):
        return self.s1 + self.s2
    def cıkar(self):
        return self.s1 - self.s2
    def carp(self):
        return self.s1 * self.s2

mat = Mat(3,6)
sonuc1 = mat.topla()
sonuc2 = mat.cıkar()
sonuc3 = mat.carp()
print("toplama sonucu : " + str(sonuc1))
print("çıkarma sonucu : " + str(sonuc2))
print("çarpma sonucu " + str(sonuc3))

class Ist(Mat):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1,sayi2)
    def varyanHesapla(self):
        return self.s1*self.s2

istatislik = Ist(5,10)
cevap = istatislik.topla()
print("cevap : " + str(cevap))

##inheritance