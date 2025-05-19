# Şarkı QR Oluşturucu

Bu Python projesi, kullanıcının girdiği şarkı ismine göre YouTube'da arama yapar ve bulunan ilk şarkının bağlantısını QR koda dönüştürür. QR kod, uygulama arayüzünde görsel olarak gösterilir ve yerel diske kaydedilir (`sarki_qr.png`).

## Özellikler

- PyQt5 ile oluşturulmuş kullanıcı arayüzü
- YouTube'da şarkı arama (youtube-search-python)
- QR kod üretimi (qrcode kütüphanesi)
- QR kodun GUI'de gösterilmesi

## Gereksinimler

Aşağıdaki kütüphanelerin kurulu olması gerekir:

```bash
pip install PyQt5 qrcode youtube-search-python
