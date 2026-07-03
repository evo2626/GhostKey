#!/usr/bin/env python3
# GhostKey - Şifreleme Projesi
# Kullanım: python3 ghostkey.py
# core/engine.py ghost key motorunun inşası


# Motoru ve dosya işlemlerini yapan sınıfları dışarıdan içeri alıyoruz.
from core.engine import GhostKeyEngine 
from core.file_handler import FileEncryptor
from core.security import get_file_hash
import base64 

class GhostKeyApp: # Ana yönetim sınıfı: Programın beyni.
    def __init__(self, anahtar): # Uygulamayı başlatırken anahtarı alıyoruz.
        self.anahtar = anahtar
        # core/engine.py içindeki XOR motorumuzu aktif ediyoruz.
        self.engine = GhostKeyEngine(anahtar) 
        # Dosya kargocusunu (file_handler) hazırlıyoruz.
        self.dosya_isleyici = FileEncryptor(anahtar)

    def calistir(self): # Menü ve kullanıcı etkileşimi burada.
        print("--- GhostKey Güvenlik Sistemi (XOR Aktif) ---")
        print("1: Metin Şifrele")
        print("2: Şifreli Metni Çöz")
        print("3: Dosya Şifrele")
        print("4: Dosya Çöz")
        secim = input("Seçiminiz (1-4): ")
        
        if secim == "1":
            metin = input("Şifrelenecek Metin: ")
            sifreli = self.engine.process(metin)
            # Base64 ile şifreli metni kopyalanabilir yapıyoruz
            base64_sifreli = base64.b64encode(sifreli.encode('utf-8', errors='replace')).decode('utf-8')
            print("Sonuç (Kopyala ve Gönder):", base64_sifreli)

        elif secim == "2": # Şifreli Metni Çöz
            kod = input("Çözülecek (Base64) Metni Yapıştır: ")
            # Base64'ten çözerek geri alıyoruz
            sifreli_bayt = base64.b64decode(kod.encode('utf-8')).decode('utf-8', errors='replace')
            cozulmus = self.engine.process(sifreli_bayt)
            print("Çözülmüş Metin:", cozulmus)

        elif secim == "3": # Dosya Şifrele
            yol = input("Şifrelenecek dosya yolu: ")
            yeni_dosya = self.dosya_isleyici.encrypt_file(yol)
            hash_degeri = get_file_hash(yeni_dosya)
            print(f"Şifrelendi: {yeni_dosya} | Hash: {hash_degeri}")

        elif secim == "4": # Dosya Çöz
            yol = input("Çözülecek dosya yolu: ")
            cozulmus = self.dosya_isleyici.decrypt_file(yol)
            print(f"Dosya başarıyla çözüldü: {cozulmus}")

        else: 
            print("[!] HATA: Geçersiz seçim! Lütfen 1, 2, 3 veya 4 girin.")

if __name__ == "__main__":
    # Program buradan başlar. Anahtarını burada belirleyebilirsin.
    app = GhostKeyApp("Ghost2026")
    app.calistir()
              





 
