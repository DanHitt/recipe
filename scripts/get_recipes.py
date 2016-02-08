import csv
import os
import sys
import requests
from slugify import slugify
from PIL import Image 
import urllib
from django.core.files import File 

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe.settings")
import django

django.setup()

from main.models import Recipe, Ingredient


Recipe.objects.all().delete()
Ingredient.objects.all().delete()

api_key = '74ccfd763feb154ff62f637b5250bc69'
param_dict = {'key': api_key, 'sort': 'r', 'page': '1'}
response = requests.get('http://food2fork.com/api/search/recipes.json', params=param_dict)

# print response
response = response.json() 
recipes = response['recipes']


for recipe in recipes:
	a = recipe['title']
	recipe_id = recipe['recipe_id']
	param_dict = {'key': api_key, 'rId':recipe_id}
	response = requests.get('http://food2fork.com/api/get', params=param_dict)
	response = response.json()
	# print response
	ingredients = response['recipe']['ingredients']
	# print "*****"
	# print ingredients
	new_recipe, created = Recipe.objects.get_or_create(name=recipe['title'])
	print recipe
	print created
	print '******'
	print ingredients
	new_recipe.name = recipe['title']
	new_recipe.slug = slugify(recipe['title'])
	print new_recipe.name
	new_recipe.save()

	image = urllib.urlretrieve(recipe['image_url'])
	print "999999"
	print image
	print "9999999"
	x = os.path.basename
	print x
	new_recipe.image.save(os.path.basename(recipe['image_url']), File(open(image[0])))

	for ingredient in ingredients:
		print "*****"
		print ingredient
		new_ingredient, created = Ingredient.objects.get_or_create(name=ingredient)
		print "NEW INGREDIENT"
		print new_ingredient.name
		new_recipe.ingredients.add(new_ingredient)
		new_ingredient.save()

	# new_ingredient, created = Ingredient.objects.get_or_create(name=ingredients['ingredients'])
	# new_ingredient.save()


