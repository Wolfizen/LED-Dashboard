from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
	path('', views.RootPageView.as_view(), name='root'),
	path('control/', views.StripControlFormSubmit.as_view(), name='strip-control'),
	path('set-profile/', views.ProfileSelectFormSubmit.as_view(), name='set-profile'),
]
