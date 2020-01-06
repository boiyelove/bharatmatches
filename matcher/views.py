from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from profiles.models import Profile
from .models import Match

User = get_user_model()

@receiver(user_logged_in)
def get_user_matches_receiver(sender, request, user, *args, **kwargs):
	for u in User.objects.exclude(username=user.username).order_by("-id")[:200]:
		profile = Profile.objects.get_or_create(user=u)
		matched, created = Match.objects.get_or_create_match(user_a=u,user_b=user)





# def location_match_view(request, slug):
# 	try:
# 		instance = Location.objects.get(slug=slug)
# 	except Location.MultipleObjectsReturned:
# 		queryset = Location.objects.filter(slug=slug).order_by('-id')
# 		instance = queryset[0]
# 	except Location.DoesNotExist:
# 		raise Http404

# 	template = "matches/location_match_view.html"
# 	context = {
# 		"instance": instance,
# 	}
# 	return render(request, template, context)