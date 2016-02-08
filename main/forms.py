from django import forms 
from .models import Recipe, Ingredient



class RecipeForm(forms.ModelForm):
	# holder = forms.CharField(label='Your Name', max_length=40, error_messages={'required':'dummy'})
	# play = forms.CharField(label='The Play', max_length=40)
	# price = forms.IntegerField(label='Ticket Price')


	class Meta:
		model = Recipe
		fields = ('name', 'directions', 'image')
		labels = {
			'name': ('Your Recipe Name') #, 'play': ('Your Play Choice'), 'price': ('Ticket Price'),
		}

		# error_messages = {'holder': {'ValueError': ('put something'),},}

		# def __init__(self, *args, **kwargs):
		# 	placeholder = kwargs.pop("dynamic_placeholder")
		# 	super(CompleteRegistrationForm, self).__init__(*args, **kwargs)
		# 	self.fields['message'].placeholder = placeholder

