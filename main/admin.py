from django.contrib import admin
from .models import Ingredient, Recipe

class IngredientAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class RecipeAdmin(admin.ModelAdmin):
	list_display = ('name', 'directions')
	search_fields = ('name',)





admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)