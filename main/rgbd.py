import json
import logging
import os

from django.conf import settings

log = logging.getLogger(__name__)


class Profile(object):
	def __init__(self, name):
		self.name = name
		self.path = os.path.join(settings.RGBD_CONFIG_DIR, name + '.json')

	def validate(self):
		if os.path.exists(self.path):
			with open(self.path) as fp:
				json.load(fp)  # Verify the JSON file is valid
		else:
			raise ValueError("Profile '{}' does not exist".format(self.name))


def find_profiles():
	strip_profiles = []
	if os.path.exists(settings.RGBD_CONFIG_DIR):
		for fname in os.listdir(settings.RGBD_CONFIG_DIR):
			if fname.endswith('.json') and fname.rstrip('.json') not in settings.RGBD_EXCLUDE_PROFILES:
				try:
					profile = lookup_profile(fname.rstrip('.json'))
					strip_profiles.append(profile)
				except ValueError:
					continue
	else:
		log.warning("The rgbd config directory '{}' does not exist!".format(settings.RGBD_CONFIG_DIR))
	return strip_profiles


def lookup_profile(name):
	profile = Profile(name)
	profile.validate()
	return profile


def set_brightness(value):
	if 0 <= value <= 255 and isinstance(value, int):
		# TODO: switch to DBUS
		os.system('/home/rgb_user/.local/bin/lightctl set-brightness {}'.format(value))
	else:
		raise ValueError("Bad range")


def switch_to_profile(profile):
	# TODO: switch to DBUS
	profile.validate()
	os.system('/home/rgb_user/.local/bin/lightctl load-conf {}'.format(profile.path))
