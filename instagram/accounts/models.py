from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    username = models.CharField(max_length=20, blank=True)
    follows = models.ManyToManyField('self', through='Follow', related_name='followed', blank=True, symmetrical=False)

    def __str__(self):
        return 'id=%d, user_id=%d, college=%s, major=%s' % (self.id, self.user.id, self.college, self.major)

    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Follow(models.Model):
  follow_from = models.ForeignKey(Profile, related_name='follow_to', on_delete=models.CASCADE)
  follow_to = models.ForeignKey(Profile, related_name='follow_from', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s follows %s' % (self.follow_from, self.follow_to)
