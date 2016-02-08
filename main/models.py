from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from main.slug import unique_slugify





class Ingredient(models.Model):
	name = models.CharField(max_length=250)


	def __unicode__(self):
		return self.name



class Recipe(models.Model):
	name = models.CharField(max_length=70)
	ingredients = models.ManyToManyField(Ingredient)
	directions = models.TextField(null=True, blank=True)
	slug = models.SlugField(max_length=200, unique=True)
	description = models.URLField(null=True, blank=True)#link to outside direction
	image = models.ImageField(upload_to='media', blank=True)




	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('main.views.list_recipes')

	def save(self):
		slug = '%s' % (self.name)
		unique_slugify(self, slug)
		super(Recipe, self).save()

