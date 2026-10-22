# ==============================================================================
# KAPSÜLLEME (ENCAPSULATION) - ÖĞRENCİ ÇALIŞMA DOSYASI
# ==============================================================================

class BankaHesabi:
    def __init__(self, hesap_sahibi, ilk_bakiye):
        self.hesap_sahibi = hesap_sahibi
        
        self.____bakiye = ilk_bakiye 

    def bakiye_goster(self):
        return f"Sayın {self.hesap_sahibi}, güncel bakiyeniz: {self.____bakiye} TL"

    def para_yatir(self, miktar):
        if miktar > 0:
            self.____bakiye += miktar
            return f"{miktar} TL yatırıldı. Yeni bakiye: {self.____bakiye} TL"
        else:
            return "HATA: Yatırılacak miktar 0'dan büyük olmalıdır!"

class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        
        self.____sifre = sifre

    def sifre_degistir(self, eski_sifre, yeni_sifre):
        if eski_sifre == self.____sifre:
            if len(yeni_sifre) >= 6:
                self.____sifre = ____
                return "Başarılı: Şifreniz güvenli bir şekilde güncellendi."
            else:
                return "HATA: Yeni şifre en az 6 karakter olmalıdır!"
        else:
            return "HATA: Eski şifrenizi yanlış girdiniz! İşlem reddedildi."