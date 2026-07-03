#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class GhostKeyEngine: # Şifreleme işlemlerini yürüten ana sınıfı tanımlıyoruz.
    def __init__(self, anahtar): # Motoru ilk çalıştırdığımızda anahtarı kaydediyoruz.
        self.anahtar = anahtar # Anahtarı 'self' ile sınıfın belleğine alıyoruz.

    def process(self, veri, mode='encrypt'): # Şifreleme ve çözme işleminin yapıldığı ana fonksiyon.
        sonuc = "" # İşlenmiş metni depolamak için boş bir kutu oluşturuyoruz.
        
        # 'enumerate' metindeki her harfi sırasıyla (i) ve değeriyle (char) beraber verir.
        for i, char in enumerate(veri): 
            
            # '% len(self.anahtar)': Anahtar kısa olsa bile metnin sonuna kadar dönmesini sağlar.
            key_char = self.anahtar[i % len(self.anahtar)] 
            
            # 1. ord(char): Harfi bilgisayarın anladığı sayıya (ASCII) çevirir.
            # 2. ^ (XOR): Sayıyı anahtarın sayısal değeriyle matematiksel olarak karıştırır.
            # 3. chr(): Çıkan sonucu tekrar okunabilir bir harfe dönüştürür.
            sonuc += chr(ord(char) ^ ord(key_char)) 
        return sonuc # Şifrelenmiş veya çözülmüş metni geri gönderiyoruz.

