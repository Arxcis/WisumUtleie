from django.db import models

"""
	Django model field-types:
		models.Charfield(max_length=int) - A string field, for small- to large-sized strings."
		models.TextField() - A large text field.
		models.DateTimeField(auto_now=bool) - A date and time, represented in Python by a datetime.datetime instance. "
		models.UrlField(max_length=int) - A CharField for URL
		models.EmailField() - A CharField that checks that the value is a valid email address. 
		models.IntegerField() - 32bit integer

		models.FielField() - A file-upload field
		models.ImageField() - Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image
"""


class GenericItem(models.Model):

	title = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	holder = models.CharField(max_length = 50)

	status = models.CharField(max_length = 20)
	status_int = models.IntegerField()

	image1 = models.ImageField()
	image2 = models.ImageField()
	image3 = models.ImageField()





