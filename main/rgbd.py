import json
import logging
import os

from django.conf import settings

log = logging.getLogger(__name__)


class Profile(object):
	def __init__(self, name):
		self.name = name
		self.path = os.path.join(settings.RGBD_CONFIG_DIR, name + '.json')


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
	if os.path.exists(profile.path):
		with open(profile.path) as fp:
			json.load(fp)  # Verify the JSON file is valid
		return profile
	else:
		raise ValueError("Profile '{}' does not exist".format(name))
