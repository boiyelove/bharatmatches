from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MatchUser, BannedEmail, MatchUserPreference, MatchUserAddress, MatchUserProfile
from .utils import calculate_age

class RegistrationForm(UserCreationForm, forms.ModelForm):

	class Meta(UserCreationForm.Meta):
		model =  MatchUser
		fields = ('first_name', 'last_name', 'date_of_birth', 'email', 'password1', 'password2')
		widgets = {
			'date_of_birth': forms.TextInput(attrs={'type':'date'})
		}


	def clean_date_of_birth(self):
		cleaned_data = self.cleaned_data
		email = super().clean().get('email')
		
		# print('in clean dob, email is', email)
		# if not email:
		# 	raise forms.ValidationError('Please enter a valide email address')

		print('self.cleaned_data in clean is', cleaned_data)
		email = cleaned_data.get('email')
		dob = cleaned_data.get('date_of_birth')
		print('in clean dob, email is', email)
		if calculate_age(dob) < 18:
			# BannedEmail.objects.create(email=email, reason='User below required age')
			raise forms.ValidationError("Minimum registeration age is 18 years")
		return dob

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if BannedEmail.objects.filter(email=email):
			raise forms.ValidationError('Sorry this email is no longer allowed to register, please contact admin')
		return email.strip()


	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.username = (self.cleaned_data['email']).replace('@', '').replace('.', '').replace('-', '').replace('_','')
		if commit:
			user.save()
			return user


class PreferenceForm(forms.ModelForm):
	class Meta:
		model =  MatchUserPreference
		fields = ('age_lower', 'age_higher', 'states')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model =  MatchUserProfile
		fields = ('marital_status', 'gender')

class UserAddressForm(forms.ModelForm):
	class Meta:
		model =  MatchUserAddress
		fields = ('city', 'state', 'country')

class UserBioForm(forms.ModelForm):
	class Meta:
		model = MatchUserProfile
		fields = ('bio',)