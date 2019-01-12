from django.urls import path
from . import views


urlpatterns = [
	path('', views.RootPageView.as_view(), name='root'),
]
