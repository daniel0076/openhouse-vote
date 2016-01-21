from django.db import models
from django.core.validators import RegexValidator,MinLengthValidator,validate_email


def validate_mobile(string):
    RegexValidator(regex='^\d{10}$',message='格式：0987654321')(string)
# Create your models here.

class Candidates(models.Model):
	class Meta:
		verbose_name = "候選作品"
		verbose_name_plural = "候選作品"

	logo=models.ImageField(u"作品圖片",upload_to = 'logos')
	concept=models.TextField(u"設計理念")

class Voter(models.Model):
	class Meta:
		verbose_name = "投票人"
		verbose_name_plural = "投票人"

	Identity= (
			(u'在校學生', u'在校學生'),
			(u'校友', u'校友'),
			(u'教職員工', u'教職員工'),
			)

	name= models.CharField(u'姓名', max_length=30)
	identity= models.CharField(u'身份', max_length=10, choices=Identity)
	idno = models.CharField(u'學號/工號/身份證字號',primary_key=True,max_length=10)  # AutoField
	email= models.EmailField(u'Email')
	cellphone= models.CharField(u'手機號碼',max_length=10,validators=[validate_mobile],help_text='手機')
