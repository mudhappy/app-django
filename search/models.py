from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

  STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published'),
  )

  author = models.ForeignKey('auth.User')
  title = models.DateField(blank=True, null=True, default=timezone.now)
  body = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateField(auto_now=True)
  published_date = models.DateField(blank=True, null=True, default=timezone.now)

  status = models.CharField(max_length=20, choices = STATUS, default='draft')

  def publish(self):
    self.published_date = timezone.now
    self.status = 'published'
    self.save()

  def __str__(self):
    return self.title