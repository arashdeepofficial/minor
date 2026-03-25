from django.db import models
from django.conf import settings
from events.models import Event
import qrcode
from io import BytesIO
from django.core.files import File

User = settings.AUTH_USER_MODEL

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    attended = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        qr_data = f"{self.user.id}-{self.event.id}"
        qr_img = qrcode.make(qr_data)

        buffer = BytesIO()
        qr_img.save(buffer, format='PNG')

        self.qr_code.save(f'qr_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)
