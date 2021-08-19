from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.widgets import DateInput, DateTimeInput, PasswordInput
from app1 import models
class Register(forms.ModelForm):
    class Meta:
        model=User
        widgets={'password':PasswordInput()}
        fields=["first_name","last_name","username","email"]
        
class Notes(forms.ModelForm):
    class Meta:
        model=models.Notes
        fields=["title","description"]
class DateInput(forms.DateInput):
    input_type="date"
class Homework(forms.ModelForm):
    class Meta:
        model=models.Homework
        widgets={"due":DateInput()}
        fields=["subject","title","description","due"]
class Todo(forms.ModelForm):
    class Meta:
        model=models.Todo
        fields=["data"]
class search(forms.Form):
    data=forms.CharField(max_length=100,label="Enter Your Search :")