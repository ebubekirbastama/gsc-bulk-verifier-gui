# 🧩 GSC Bulk Verifier GUI

Google Search Console (GSC) için birden fazla domaini toplu şekilde ekleyip doğrulayan Python tabanlı, modern bir GUI (grafik arayüz) uygulaması.

Bu araç, elinizdeki domain listesine göre her bir domaini Search Console’a ekler ve HTML dosyasıyla doğrulama işlemini yapar. Elinizde daha önceden doğrulama dosyaları sunuculara yüklenmiş olmalıdır.

---

## 🚀 Özellikler

- ✅ Google Search Console API üzerinden domainleri toplu ekler  
- ✅ Site Verification API ile `HTML dosyası yöntemi` üzerinden doğrulama yapar  
- ✅ Basit ve kullanıcı dostu Tkinter GUI arayüzü  
- ✅ Tüm işlem sonuçlarını log penceresinde gösterir  
- ✅ `domainler.txt` ve `service-account.json` dosyasıyla çalışır  

---

## 📷 Ekran Görüntüsü

(Tkinter GUI ekran görüntüsünü burada paylaşabilirsiniz)

---

## 📦 Gereksinimler

- Python 3.7+
- Google Cloud'dan alınmış bir `service-account.json`
- Domainlerin yer aldığı bir `domainler.txt` dosyası

Kurulum:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

## 📁 Dosya Yapısı

```
gsc-bulk-verifier-gui/
├── gsc_gui_tool.py         # Ana Python GUI uygulaması
├── domainler.txt           # Her satıra bir domain
├── service-account.json    # Google API erişim anahtarınız
└── README.md               # Bu döküman
```

---

## 📝 Kullanım

1. `domainler.txt` dosyasına her satıra bir domain olacak şekilde yazın.  
   Örnek:
   ```
   example.com
   www.siteniz.net
   ```

2. `service-account.json` dosyasını Google Cloud Console üzerinden oluşturun:
   - GSC API (webmasters) ve Site Verification API aktif olmalı  
   - Service Account’a `Search Console` erişim izni verilmeli  

3. Uygulamayı çalıştırın:
   ```bash
   python gsc_gui_tool.py
   ```

4. GUI üzerinden:
   - Domain listesini yükleyin
   - API JSON dosyasını seçin
   - “GSC Ekle ve Doğrula” butonuna tıklayın

---

## ⚠️ Önemli Notlar

- Bu araç `HTML file verification` yöntemini kullanır.
- GSC doğrulama dosyaları (`googleXXXX.html`) her domainin kök dizininde mevcut olmalıdır.
- Bu araç doğrulama dosyasını sunucuya **yüklemez**, sadece doğrulama adımını tetikler.

---

## 📄 Lisans

MIT Lisansı  
Bu proje açık kaynak olarak sunulmuştur. Katkılarda bulunmaktan çekinmeyin.

---

## 👨‍💻 Katkı

Pull request’ler ve issue’lar memnuniyetle karşılanır. Hataları veya önerileri iletmekten çekinmeyin.
