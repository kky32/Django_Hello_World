from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):

    # One way street. When user is deleted, profile is also deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Upload image
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # REDUCE uploaded image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open uploaded image
        img = Image.open(self.image.path)

        # Reduce to 300x300
        if img.height > 300 or img.width > 300:
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save(self.image.path)


