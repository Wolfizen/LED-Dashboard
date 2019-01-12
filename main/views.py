import json
import logging
import os

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from main.forms import StripControlForm, ProfileSelectForm

log = logging.getLogger(__name__)


class RootPageView(TemplateView):
	template_name = 'main/root.html'

	def get_strip_profiles(self):
		strip_profiles = {}
		if os.path.exists(settings.RGBD_CONFIG_DIR):
			for f in os.listdir(settings.RGBD_CONFIG_DIR):
				if os.path.isfile(f) and f.endswith('.json'):
					try:
						with open(f) as fp:
							json.load(fp)  # Verify the JSON file is valid
							profile = object()
							profile.name = f.rstrip('.json')
							profile.path = os.path.join(settings.RGBD_CONFIG_DIR, f)
							strip_profiles[profile.name] = profile
					except ValueError as e:
						continue
		else:
			log.warning("The rgbd config directory '{}' does not exist!".format(settings.RGBD_CONFIG_DIR))
		return strip_profiles

	def get_context_data(self, **kwargs):
		context = super(RootPageView, self).get_context_data(**kwargs)

		control_form = StripControlForm()
		context['control_form'] = control_form

		strip_profiles = self.get_strip_profiles()
		for profile in strip_profiles.values():
			profile.form = ProfileSelectForm(profile.name)
		context['strip_profiles'] = strip_profiles

		return context


class StripControlFormSubmit(View):

	def post(self, request):
		form = StripControlForm(request.POST)
		if form.is_valid():
			# TODO!
			print("Strip control submit: {}".format(request.POST))
			return HttpResponseRedirect(reverse('main:root'))
		else:
			return HttpResponseBadRequest()


class ProfileSelectFormSubmit(View):

	def post(self, request):
		form = ProfileSelectForm(request.POST)
		if form.is_valid():
			# TODO!
			print("Profile select submit: {}".format(request.POST))
			return HttpResponseRedirect(reverse('main:root'))
		else:
			return HttpResponseBadRequest()

