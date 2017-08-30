from django import forms
from Survey.models import office,intro 
from django.contrib import admin


class officeForm(forms.ModelForm):
	class Meta:
		model = office
		fields = ['R1B1','R1B2','R1B3','R2B1','R2B2','R2B3','R3B1','R3B2','R3B3',]
		

class introForm(forms.ModelForm):
	class Meta:
		model = intro
		fields = ['name','education','sex',]
		
		
