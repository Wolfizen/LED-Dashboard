from django import forms


class StripControlForm(forms.Form):
	power = forms.BooleanField(label="Power", initial=True, required=False)
	brightness = forms.IntegerField(label="Brightness", initial=128, required=False)
	reset = forms.BooleanField(label="Reset", initial=False, required=False, widget=forms.HiddenInput())

	def __init__(self, power=None, brightness=None, **kwargs):
		super(StripControlForm, self).__init__(**kwargs)
		if power is not None:
			self.fields['power'].initial = power
		if brightness is not None:
			self.fields['brightness'].initial = brightness


class ProfileSelectForm(forms.Form):
	profile = forms.CharField(label="Profile", widget=forms.HiddenInput())

	def __init__(self, profile_name=None, **kwargs):
		super(ProfileSelectForm, self).__init__(**kwargs)
		self.fields['profile'].initial = profile_name
