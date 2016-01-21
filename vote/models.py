from django.db import models

# Create your models here.

class Candidates(models.Model):
	class Meta:
		verbose_name = "候選作品"
		verbose_name_plural = "候選作品"

	logo=models.ImageField(u"作品圖片",upload_to = 'logos')
	concept=models.TextField(u"設計理念")


