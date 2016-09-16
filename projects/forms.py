from django import forms
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.auth.models import User

class ProjectForm(forms.Form):
	project_title = forms.CharField(max_length = 500)
	description = forms.CharField(max_length = 5000)
	# photos = ArrayField(forms.FileField(), null = True)
	photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
