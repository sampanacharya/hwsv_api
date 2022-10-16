from django.db import models

# Create your models here.
def nameFile(instance, filename):
	return '/'.join(['images',str(instance.name), filename])

class UploadImageTest(models.Model):
	name = models.CharField(max_length = 100)
	image = models.FileField(upload_to='images/')
	 