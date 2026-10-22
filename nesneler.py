
from siniflar_ogrenci import BankaHesabi, Kullanici

print("*" * 50)
print("SEVİYE 1: BANKA HESABI (Temel Kapsülleme)")
print("*" * 50)

benim_hesabim = BankaHesabi("__________", ______)

print(benim_hesabim.____________())

print(benim_hesabim.____________(____))


print("\n" + "*" * 50)
print("SEVİYE 2: KULLANICI ŞİFRESİ (Kontrollü Kapsülleme)")
print("*" * 50)

benim_uyeligim = Kullanici("__________", "123456")

print("Yanlış Şifre Denemesi:")
print(benim_uyeligim.____________("yanlis_eski", "yeniSifre123"))

print("\nDoğru Şifre Değiştirme:")
print(benim_uyeligim.____________("________", "________"))