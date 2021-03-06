from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import Profile

class Feed(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='feed_photos')
    like_users = models.ManyToManyField(User, blank=True, related_name='like_feeds', through='Like')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.author


class FeedComment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

