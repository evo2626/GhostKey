#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# core/file_handler.py

# engine.py dosyamızdan GhostEngine sınıfını çağırıyoruz. 
# Bu sayede file_handler, matematiği nasıl yapacağını öğrenmiş oluyor.
from core.engine import GhostKeyEngine

class FileEncryptor:
    def __init__(self, anahtar): # Sınıf başlatılırken 'anahtar' bilgisini alıyoruz.
        self.engine = GhostKeyEngine(anahtar) # 'self.engine' diyerek, motoru bu sınıfın içine bir araç olarak ekliyoruz.

    # Dosya şifreleme fonksiyonu
    def encrypt_file(self, dosya_yolu): 

        with open(dosya_yolu, 'r', encoding='utf-8') as f: # 'r' modu dosyayı sadece okumak için açtığımızı belirtir.  
            veri = f.read() # Dosyanın tüm içeriğini okuyup 'veri' değişkenine alıyoruz.

        sifreli_veri = self.engine.process(veri, mode='encrypt') # 'self.engine.process' diyerek okuduğumuz veriyi motora gönderiyoruz.
        # 'mode' kısmını 'encrypt' yaparak motorun şifreleme yapmasını sağlıyoruz.

        # Şifreli veriyi yeni bir dosyaya yazıyoruz (.locked uzantısı ile).
        yeni_dosya = dosya_yolu + ".locked" # Yeni dosya adı, orjinal dosya adı + ".locked" olacak.
        with open(yeni_dosya, 'w', encoding='utf-8') as f: # 'w' modu dosyayı yazmak için açtığımızı belirtir. 
            f.write(sifreli_veri) # Şifreli veriyi yeni dosyaya yazıyoruz. 

        return yeni_dosya # İşlem bitince yeni dosyanın adını geri veriyoruz.

# Dosya çözme fonksiyonu
    def decrypt_file(self, dosya_yolu): 
        # Şifreli dosyayı açıp içindekileri okuyoruz.
        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            sifreli_veri = f.read()

    # Motoru 'decrypt' modunda çalıştırarak veriyi tekrar okunabilir hale getiriyoruz.
        cozulmus_veri = self.engine.process(sifreli_veri, mode='decrypt')

    # Çözülen veriyi yeni bir dosyaya (örneğin: deneme.txt.locked -> deneme_cozuldu.txt) yazıyoruz.
        orjinal_dosya = dosya_yolu.replace(".locked", "_cozuldu.txt") 
        with open(orjinal_dosya, 'w', encoding='utf-8') as f: 
            f.write(cozulmus_veri) # çözülen veriyi yeni dosyaya yazıyoruz
        return orjinal_dosya #işlem bitince yeni dosyanın adını geri veriyoruz 
                                   

