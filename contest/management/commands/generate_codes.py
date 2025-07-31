import random
import string
from django.core.management.base import BaseCommand
from contest.models import Code

class Command(BaseCommand):
    help = 'Veritabanına 1 Milyon adet benzersiz çekiliş kodu üretir ve ekler.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Kod üretme işlemi başlıyor...")
        chars = string.ascii_uppercase + string.digits
        batch_size = 10000
        codes = set()

        while len(codes) < 1000000:
            codes.add(''.join(random.choice(chars) for _ in range(6)))

        code_objects = [Code(code_value=code) for code in codes]
        Code.objects.bulk_create(code_objects, batch_size=batch_size) ### toplu veritabanı oluşturmasını istiyoruz. batch_size a göre belirlenen miktarda kod oluşturur.
        self.stdout.write(self.style.SUCCESS('1 Milyon kod başarıyla üretildi ve eklendi.'))