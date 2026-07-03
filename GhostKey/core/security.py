#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib # Dosya bütünlüğünü kontrol etmek için hash kütüphanesi

def get_file_hash(dosya_yolu): 
    # Dosyayı "okuma-binary" modunda açıp SHA256 ile parmak izini çıkarıyoruz.
    sha256 = hashlib.sha256() # SHA256 şifreleme algoritmasını başlatıyoruz.
    
    with open(dosya_yolu, "rb") as f: # Dosyayı güvenli bir şekilde açıyoruz.
        while chunk := f.read(8192): # Büyük dosyaları dondurmamak için parça parça okuyoruz.
            sha256.update(chunk) # Okunan parçayı hash'e ekliyoruz.
            
    return sha256.hexdigest() # Hexadecimal formatta benzersiz bir ID dönüyoruz.

# Bu fonksiyonun amacı: Eğer dosya üzerinde 1 byte bile oynanırsa, 
# hash değeri tamamen değişir. Bu sayede dosyanın bozulup bozulmadığını anlarsın.                

