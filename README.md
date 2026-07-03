# GhostKey
GhostKey, verilerinizi XOR algoritması ile şifreleyen, dosya bütünlüğünü SHA256 ile doğrulayan modüler bir güvenlik aracıdır.

🛠 Teknik Mimari
Proje, temiz kod prensiplerine göre aşağıdaki modüllerden oluşmaktadır:

ghostkey.py: Uygulamanın ana giriş noktası ve kullanıcı etkileşim arayüzü.

core/engine.py: XOR tabanlı temel şifreleme ve deşifreleme motoru.

core/file_handler.py: Dosya okuma, şifreleme akış yönetimi ve .locked uzantılı dosya işlemleri.

core/security.py: SHA256 hashing algoritması ile dosya bütünlüğü kontrolü.

🚀 Özellikler
XOR Şifreleme: Metin ve dosya bazlı hızlı şifreleme.

Bütünlük Kontrolü: Şifrelenen dosyaların bozulmadığını garanti eden benzersiz hash değerleri.

Modüler Yapı: Kolayca genişletilebilir sınıf tabanlı mimari.

### 💻 Kullanım
Ana uygulamayı çalıştırmak için terminalde şu komutu kullanın:
python3 ghostkey.py

---> Menü üzerinden ihtiyacınız olan işlevi (Metin/Dosya Şifrele/Çöz) seçin.

🛡 Uyarı
Bu araç eğitim amaçlı geliştirilmiştir. Şifreleme anahtarınızı (key) kaybetmeniz durumunda, şifrelenmiş dosyalara erişim mümkün olmayacaktır. Lütfen kritik verileriniz üzerinde denemeler yaparken yedek almayı unutmayın.
