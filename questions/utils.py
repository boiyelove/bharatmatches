import os
from django.conf import settings
from .models import Question


def import_questions():
	dirr = os.path.join(settings.BASE_DIR, '.env/date-questions.md')
	with open(dirr, 'r') as file:
		for line in file:
			Question.objects.create(text=line)
			print(line)