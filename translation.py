class Translation(object):
    START_TEXT = """Merhaba {},
Ben bir URL Yükleyicisiyim!
Bu Botu kullanarak HTTP/HTTPS bağlantılarını yükleyebilirsiniz!
daha fazla bilgi için /help!"""
    FORMAT_SELECTION = "İstediğiniz formatı seçin: <a href='{}'>dosya boyutu yaklaşık olabilir</a> \nKapak fotoğrafı ayarlamak istiyorsanız, aşağıdaki düğmelerden herhangi birine dokunmadan önce veya hızlı bir şekilde fotoğraf gönderin.\nKapak fotoğrafını silmek için /delthumb kullanabilirsiniz."
    SET_CUSTOM_USERNAME_PASSWORD = """Premium videoları indirmek istiyorsanız, aşağıdaki formatı sağlayın:
URL | dosyaadı | kullanıcıadı | şifre"""
    DOWNLOAD_START = "Şimdi İndiriliyor.."
    UPLOAD_START = "Şimdi Yükleniyor.."
    RCHD_TG_API_LIMIT = "{} saniye içinde İndirildi.\nAlgılanan Dosya Boyutu: {}\nÜzgünüm. Ancak, TELEGRAM API sınırlamaları nedeniyle 2GB'DEN büyük dosyaları yükleyemiyorum."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "@tiranozorbot'u kullandığınız için teşekkürler)"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "{} saniye içinde İndirildi.\n{} saniye içinde yüklendi.\n\n@tiranozorbot"
    SAVED_CUSTOM_THUMB_NAIL = "✅ Video/Dosya için kapak fotoğrafı kaydedildi. Bu görüntü video/dosya için kullanılacaktır."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Kapak fotoğrafı başarıyla temizlendi."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "HATA...\n<b>YouTubeDL</b>: {}"
    HELP_USER = """Nasıl kullanılırım? Aşağıdaki adımları izleyin!
    
1. URL gönderin (örnek.domain/Dosya.mp4 | Yeni DosyaAdı.mp4).
2. Kapak fotoğrafı için fotoğraf gönderin (İsteğe bağlı).
3. Buton seçin.
   SVideo - Ekran görüntüleri ile video olarak verir
   DFile  - Ekran görüntüleri ile dosya olarak verir
   Video  - Ekran görüntüsü olmadan video olarak verir
   File   - Ekran görüntüsü olmadan dosya verir
Bot cevap vermediyse @thebans ile iletişime geçin"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Kapak fotoğrafı oluşturmak için bir medya albümüne /genthumb komutunu yanıtlayın"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Albüm sadece iki fotoğraf içermelidir. Lütfen albümü yeniden gönderin ve tekrar deneyin veya bir albümde yalnızca iki adet fotoğraf gönderin."""
    CANCEL_STR = "İşlem İptal Edildi"
    ZIP_UPLOADED_STR = "{} Dosyası {} saniye içinde yüklendi"
    SLOW_URL_DECED = "Tanrım, çok yavaş bir URL gibi görünüyor. Evimi mahvettiğin için bu dosyayı indirecek havamda değilim. Bu arada, neden bunu denemiyorsun?:==> https://shrtz.me/PtsVnf6 buradan bana hızlı bir URL alın, böylece yavaşlamadan Telegram'a yükleyebilirim."
