from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import calculate_age, COUNTRY_CHOICES, MOTHERTONGUE_CHOICES, RELIGION_CHOICES, CASTE_CHOICES, GOTHRAM_CHOICES, DOSHAM_CHOICES, EDUCATION_CHOICES 
# from model_utils import TimeStampedModel

# Create your models here.

class MatchUser(AbstractUser):
	date_of_birth = models.DateField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)

	def get_age(self):
		return calculate_age(self.dob)



class BannedEmail(models.Model):
	email = models.EmailField()
	reason = models.CharField(max_length=150)

class State(models.Model):
	title = models.CharField(max_length=120)

class MatchUserPreference(models.Model):
	age_lower = models.PositiveIntegerField(default=18)
	age_higher = models.PositiveIntegerField(default=62)
	states = models.ManyToManyField('State')

class MatchUserProfile(models.Model):
	user = models.OneToOneField(MatchUser, on_delete=models.CASCADE)
	gender = models.CharField(max_length=2, choices = COUNTRY_CHOICES)
	marital_status = models.CharField(max_length=2, choices = COUNTRY_CHOICES)
	bio = models.TextField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)

	def answered_check(self):
		answer_count = UserAnswer.objects.filter(user = self.id).count()
		if answer_count > 10:
			return True
		return False


class MatchUserAddress(models.Model):
	user = models.OneToOneField(MatchUserProfile, on_delete=models.CASCADE)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	country  = models.CharField(max_length=2, choices = COUNTRY_CHOICES)

# class ExtraProfile(models.Model):
# 	mother_tongue = models.CharField(max_length=6, choices=MOTHERTONGUE_CHOICES)
# 	religion = models.CharField(max_length=4, choices=RELIGION_CHOICES)
# 	caste = models.CharField(max_length=4, choices=CASTE_CHOICES)
# 	gothram = models.CharField(max_length=4, choices=GOTHRAM_CHOICES)
# 	dosham = models.CharField(max_length=4, choices=DOSHAM_CHOICES)
# 	education = models.CharField(max_length=4, choices=EDUCATION_CHOICES)
# 	profession = models.CharField(max_length=150)


class MatchUserPhoto(models.Model):
	user = models.ForeignKey(MatchUser, on_delete = models.CASCADE)
	image = models.ImageField(upload_to='userimages')
