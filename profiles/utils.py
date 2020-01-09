import requests
from datetime import date
from dateutil.relativedelta import relativedelta
from . import models


def calculate_age(born):
	print('born is', born)
	age = relativedelta(date.today(), born).years
	print('age is', age)
	return age


def populate_states():
	response = requests.get('https://countryrestapi.herokuapp.com/in/')
	response = response.json()
	for state in response['states']:
		obj, created = models.State.objects.get_or_create(title = state)

COUNTRY_CHOICES = tuple()
MOTHERTONGUE_CHOICES = tuple()
RELIGION_CHOICES = tuple()
CASTE_CHOICES = tuple()
GOTHRAM_CHOICES = tuple()
DOSHAM_CHOICES = tuple()
EDUCATION_CHOICES = (
'No schooling completed',
'Nursery school to 8th grade',
'Some high school, no diploma',
'High school graduate, diploma or the equivalent (for example: GED)',
'Some college credit, no degree',
'Trade/technical/vocational training',
'Associate degree',
'Bachelor’s degree',
'Master’s degree',
'Professional degree',
'Doctorate degree',
)
MARITAL_STATUS = (
'Single, never married',
'Married or domestic partnership',
'Widowed',
'Divorced',
'Separated',
	)
EMPLOYMENT_STATUS = (
'Employed for wages',
'Self-employed',
'Out of work and looking for work',
'Out of work but not currently looking for work',
'A homemaker',
'A student',
'Military',
'Retired',
'Unable to work'
	)

