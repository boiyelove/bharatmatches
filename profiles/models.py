from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import calculate_age
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