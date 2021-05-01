from django import forms
from djamgo.contrib.auth.models import User

class UserForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ("username", "last_name", "first_name", "email",)