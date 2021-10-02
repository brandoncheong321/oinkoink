from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Oink(models.Model):

    body = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name = 'oinks', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

class Like(models.Model):
    # note: on_delete = models.CASCADE here means if you delete a tweet, you also delete its like
    oink = models.ForeignKey(Oink, related_name = 'likes', on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, related_name = 'likes', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)