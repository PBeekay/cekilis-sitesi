from django.db import models


# Katılımcı talep ediyoruz.
class Entrant(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-posta Adresi")
    first_name = models.CharField(max_length=100, verbose_name="İsim")
    last_name = models.CharField(max_length=100, verbose_name="Soyisim")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.email


# 6 haneli unique bir kod oluşturmasını talep eiyoruz.
class Code(models.Model):
    code_value = models.CharField(max_length=6, unique=True, verbose_name="Çekiliş Kodu")
    entrant = models.ForeignKey(Entrant, on_delete=models.SET_NULL, null=True, blank=True, related_name='codes') # Her kod sadece bir kişiye atanabilir.
    def is_used(self): return self.entrant is not None
    def __str__(self): return self.code_value


### SQL kodu yazmamıza gerek olmuyor çünkü Django ya bizim için contest klasörü içerisinde Entrant ve Code tablosu oluştursun istiyoruz.

### python manage.py makemigrations konsola yazıyoruz bu komut classların veritabanında bir karşılığı var mı yok mu kontrol ediyor. ve 00001_initial.py dosyasını
### oluşturuyor.

### python manage.py migrate komutu ile de oluşturulmuş olan planları 0001.initial.py dosyasında bulunan planları inşa ediyor.

### Burada ise python talimatlarını SQL diline çeviriyor CREATE TABLE contest_entrant şeklinde.

### En sonda ise bu komutları settings.py dosyasında bulunan MySQL veritabanına gönderir.