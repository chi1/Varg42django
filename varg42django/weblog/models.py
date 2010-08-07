from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User)
	pubdate = models.DateTimeField('date published')
	heading = models.CharField(max_length=100)
	content = models.TextField()

	def __unicode__(self):
		return self.heading

