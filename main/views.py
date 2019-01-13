import logging

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from main import rgbd
from main.forms import StripControlForm, ProfileSelectForm

log = logging.getLogger(__name__)


class RootPageView(TemplateView):
	template_name = 'main/root.html'

	def get_context_data(self, **kwargs):
		context = super(RootPageView, self).get_context_data(**kwargs)

		control_form = StripControlForm()
		context['control_form'] = control_form

		strip_profiles = rgbd.find_profiles()
		for profile in strip_profiles:
			profile.form = ProfileSelectForm(profile.name)
		context['strip_profiles'] = strip_profiles

		return context


class StripControlFormSubmit(View):

	def post(self, request):
		form = StripControlForm(request.POST)
		if form.is_valid():
			brightness = form.cleaned_data['brightness']
			if not form.cleaned_data['power']:
				brightness = 0
			rgbd.set_brightness(brightness)
			print("Strip control submit: {}".format(request.POST))
			return HttpResponseRedirect(reverse('main:root'))
		else:
			return HttpResponseBadRequest()


class ProfileSelectFormSubmit(View):

	def post(self, request):
		form = ProfileSelectForm(data=request.POST)
		if form.is_valid():
			profile = rgbd.lookup_profile(form.cleaned_data['profile'])
			rgbd.switch_to_profile(profile)
			print("Profile select submit: {}".format(request.POST))
			return HttpResponseRedirect(reverse('main:root'))
		else:
			return HttpResponseBadRequest()

