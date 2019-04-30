from django.core import validators
from django.db import models


class SingletonModel(models.Model):
	"""https://steelkiwi.com/blog/practical-application-singleton-design-pattern/"""
	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		self.pk = 1
		super(SingletonModel, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		pass

	@classmethod
	def load(cls):
		obj, created = cls.objects.get_or_create(pk=1)
		return obj


class LightStrip(SingletonModel):
	power = models.BooleanField("light strip power", default=True)
	brightness = models.IntegerField(
		"brightness level",
		validators=[validators.MinValueValidator(0), validators.MaxValueValidator(255)],
		default=128)
	current_profile = models.CharField("currently selected profile", max_length=256, blank=True, null=True, default=None)

	@classmethod
	def primary_strip(cls):
		"""There's probably, very likely, almost certainly, going to be just a single strip to manage."""
		return LightStrip.load()
