from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)

    content = models.TextField()

    # ONE WAY STREET. Deleting User deletes User's posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Cannot be modified again
    date_created = models.DateTimeField(auto_now_add=True)

    # Good for updating. E.g. last_modified_field
    date_modified = models.DateTimeField(auto_now=True)

    # timezone.now
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
