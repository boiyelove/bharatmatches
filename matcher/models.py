from django.db import models
from profile.models import MatchUser

# Create your models here.
class MatchUserProfile(models.Mode):
	user = models.OneToOneField(MatchUser)
	gender = models.CharField(max_length=2, choices = COUNTRY_CHOICES)
	marital_status = models.CharField(max_length=2, choices = COUNTRY_CHOICES)
	bio = models.TextField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)


class MatchUserAddress(models.Model):
	user = models.OneToOneField(MatchUserProfile)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	country  = models.CharField(max_length=2, choices = COUNTRY_CHOICES)

class ExtraProfile(models.Model):
	mother_tongue = models.CharField(max_length=6, choices=MOTHERTONGUE_CHOICES)
	religion = models.CharField(max_length=4, choices=RELIGION_CHOICES)
	caste = models.CharField(max_length=4, choices=CASTE_CHOICES)
	gothram = models.CharField(max_length=4, choices=GOTHRAM_CHOICES)
	dosham = models.CharField(max_length=4, choices=DOSHAM_CHOICES)
	education = models.CharField(max_length=4, choices=EDUCATION_CHOICES)
	profession = models.CharField(max_length=150)


class MatchUserPhoto(models.Model):
	user = models.ForeignKey(MatchUser, on_delete = models.CASCADE)
	image = models.ImageField(uploads_to='userimages')


class Membership(models.Model):
	user = models.ForeignKey(MatchUser, on_delete=models.CASCADE)
	subscribed = models.BooleanField(default+False)
	subscription = models.ForeignKey(MatchUserSubscription, null=True)


class MatchUserSubscription(models.Model):
	author = models.ForeignKey(MatchUser, on_delete=models.CASCADE)
	date_subscribed = models.DateTimeField(auto_now_add=True)
	value = models.PositiveIntegerField(default=31)
	expiry = models.DateTimeField(null=True)


class MatchQuestion(models.Model):
	author = models.ForeignKey(MatchUser)


class MatchAnswer(models.Model):
	author = models.ForeignKey(MatchUser)
	is_yes_or_no = models.BooleanField(default=True)


class MatchAnswerOptions(models.Model):
	author = models.ForeignKey(MatchUser)


