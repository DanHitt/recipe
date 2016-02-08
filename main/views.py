from django.shortcuts import render
from django.http import JsonResponse
from .models import Recipe, Ingredient 
from django.core import serializers
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Recipe
from .forms import RecipeForm
import random



class RecipeCreate(CreateView):
	form_class = RecipeForm 
	template_name = 'recipe_form.html'





def recipe_list_API_view(request):
	recipes = Recipe.objects.all()
	for recipe in recipes:
		for ing in recipe.ingredients.all():
			print ing.id 

	output = serializers.serialize('json', recipes, fields=('name','ingredients','directions'))
	print output
	print output[0]

	return HttpResponse(output, content_type='application/json')



def base(request):

	context={}
	recipes = []
	recipes[x] = Recipe.objects.all().order_by('?')[1]
	context["recipes"] = recipes 

	return render(request, "base.html", context)



def list_recipes(request):

	context = {}
	recipes = Recipe.objects.all()
	context["recipes"] = recipes

	return render(request, "list_recipes.html", context)

def recipe_list(request):

	context = {}
	recipes = Recipe.objects.all()
	context["recipes"] = recipes

	return render(request, "recipes.html", context)



def recipes_detail(request, slug):
	# request_context=ReqestContext(request)
	context = {}
	recipe = Recipe.objects.get(slug=slug)
	ingredient_list = []
	for ingredient in recipe.ingredients.all():
		ingredient_list.append(ingredient)
	context["ingredients"] = ingredient_list
	context['recipe'] = recipe
	images = Recipe.objects.all()
	context['image'] = images 

	return render(request, "recipes_detail.html", context)



