from django import forms


class StripControlForm(forms.Form):
	power = forms.BooleanField(label="Power", initial=True, required=False)
	brightness = forms.IntegerField(label="Brightness", initial=255)


class ProfileSelectForm(forms.Form):
	profile = forms.CharField(label="Profile", widget=forms.HiddenInput())

	def __init__(self, profile_path):
		super(ProfileSelectForm, self).__init__()
		self.profile.initial = profile_path
