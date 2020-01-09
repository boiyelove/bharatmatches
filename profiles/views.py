from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import PreferenceForm, UserProfileForm, UserAddressForm, UserBioForm
from django.contrib.auth.decorators  import login_required

# Create your views here.

class PreferenceFormView(FormView):
	form_class = PreferenceForm
	# template_name = 'preference.html'
	context_object_name = 'form'
	template_name = 'forms.html'
	success_url = reverse_lazy('profile-preferences')

	# def form_valid(self, form):
	# 	form.save()
	# 	return super(PreferenceFormView)


@login_required
def profileform(request, pref=None):
	context = {	}
	if pref == 'location':context['form'] = UserAddressForm(request.POST)
	if pref == 'profile': context['form'] = UserProfileForm(request.POST)
	if pref =='bio': context['form'] =  UserBioForm(request.POST)

	template = 'forms.html'

	return render(request, template , context)