from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.forms import SimpleArrayField
# from django.db.models import ImageField
from django.db.models import FileField


def generate_filename(self, filename):
    url = "media/%s" % (filename)
    return url

# class Information(models.Model):
# 	project_title = models.CharField(max_length = 500)
# 	description = models.CharField(max_length = 5000)
# 	photos = ArrayField(models.FileField(upload_to='media'), null = True)

# 	def get_absolute_url(self):
# 		return reverse('projects:details', kwargs = {'pk': self.pk})

# 	def __str__(self):
# 		return self.project_title

class Information(models.Model):
	project_title = models.CharField(max_length = 500)
	description = models.CharField(max_length = 5000)
	# photos = ArrayField(models.FileField(upload_to='media'), null = True)

	def get_absolute_url(self):
		return reverse('projects:details', kwargs = {'pk': self.pk})

	def __str__(self):
		return self.project_title


class Images(models.Model):
	information = models.ForeignKey('Information', on_delete = models.CASCADE)
	photo = models.FileField()

	def __str__(self):
		return self.information

	













