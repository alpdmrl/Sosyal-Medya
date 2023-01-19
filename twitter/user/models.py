from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Hesap(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isim = models.CharField(max_length=100)
    soyisim = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    takip = models.ManyToManyField(User, related_name="takip")
    takipci = models.ManyToManyField(User, related_name='takipci')
    resim = models.FileField(upload_to='hesaplar/', default='default.webp', blank=True)

    def __str__(self):
        return self.user.username