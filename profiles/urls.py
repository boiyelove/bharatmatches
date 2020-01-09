from django.urls import path
from . import views
urlpatterns = [
	path('preference/', views.PreferenceFormView.as_view(), name='profile-preferences'),
	path('settings/<slug:pref>/', views.profileform, name='profile-preferences'),
]