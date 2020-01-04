from datetime import date
from dateutil.relativedelta import relativedelta


def calculate_age(born):
	print('born is', born)
	age = relativedelta(date.today(), born).years
	print('age is', age)
	return age