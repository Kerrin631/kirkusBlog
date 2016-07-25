from django import forms
from models import Blog, Category

class categoryForm(forms.Form):
	"""docstring for categoryForm"""
	title = forms.CharField(label='Category', max_length=100)
		
class postForm(forms.Form):
	
	title = forms.CharField(label = 'Title', max_length=100)
	body = forms.CharField(label = 'Post', widget=forms.Textarea)
	category = forms.ModelChoiceField(Category.objects.all())