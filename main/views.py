import logging

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from main import rgbd
from main.forms import StripControlForm, ProfileSelectForm
from main.models import LightStrip

log = logging.getLogger(__name__)


class RootPageView(TemplateView):
	template_name = 'main/root.html'

	def get_context_data(self, **kwargs):
		context = super(RootPageView, self).get_context_data(**kwargs)

		light_strip = LightStrip.primary_strip()
		context['light_strip'] = light_strip

		control_form = StripControlForm(power=light_strip.power, brightness=light_strip.brightness)
		context['control_form'] = control_form

		strip_profiles = rgbd.find_profiles()
		for profile in strip_profiles:
			profile.form = ProfileSelectForm(profile_name=profile.name)
		context['strip_profiles'] = strip_profiles

		return context


# TODO: Combine these into a single endpoint that can handle everything

class StripControlFormSubmit(View):

	def post(self, request):
		print("Strip control submit: {}".format(request.POST))
		form = StripControlForm(data=request.POST)
		if form.is_valid():
			light_strip = LightStrip.primary_strip()
			if form.cleaned_data['reset']:
				default_strip = LightStrip()
				light_strip.power = default_strip.power
				light_strip.brightness = default_strip.brightness
			else:
				light_strip.power = form.cleaned_data['power']
				light_strip.brightness = form.cleaned_data['brightness']
			# Apply the settings before saving, if there is an error the changes won't commit
			rgbd.set_brightness(light_strip.brightness if light_strip.power else 0)
			light_strip.save()
			return HttpResponseRedirect(reverse('main:root'))
		else:
			return HttpResponseBadRequest()


class ProfileSelectFormSubmit(View):

	def post(self, request):
		print("Profile select submit: {}".format(request.POST))
		form = ProfileSelectForm(data=request.POST)
		if form.is_valid():
			light_strip = LightStrip.primary_strip()
			light_strip.current_profile = form.cleaned_data['profile']
			# Apply the settings before saving, if there is an error the changes won't commit
			try:
				rgbd.switch_to_profile(rgbd.lookup_profile(light_strip.current_profile))
				light_strip.save()
				rgbd.set_brightness(light_strip.brightness if light_strip.power else 0)
			except ValueError as ex:
				log.warning("Unable to switch profiles: {}".format(str(ex)))
			return HttpResponseRedirect(reverse('main:root'))
		else:
			return HttpResponseBadRequest()

