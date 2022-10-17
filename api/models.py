from django.db import models

# Create your models here.
def nameFile(instance, filename):
	return '/'.join(['images',str(instance.name), filename])

class UploadImageTest(models.Model):
	original = models.FileField(upload_to = nameFile)
	forged = models.FileField(upload_to=nameFile)
	 