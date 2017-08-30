import json
from django.http import JsonResponse
from django.shortcuts import render
from Survey.models import office, intro
from django.http import HttpResponse
from Survey.forms import officeForm, introForm
from django.http import HttpResponseRedirect
from django.views.decorators import csrf 
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.db import connection

# Create your views here.
'''
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
'''

def get_User_Info(request):
	form = introForm(request.POST)
	print(request.method)
	if request.method == 'POST':
		form = introForm(request.POST)
		if form.is_valid():			
			name = request.POST['name']
			print(name)
			sex = request.POST['sex']
			education = request.POST['education']
			intro.objects.create(
				name = name,
				sex = sex,
				education = education
			)
			intro.save()
			print (connection.queries)
		 
			return HttpResponseRedirect("/vote/")
	return render(request, 'index.html', {'introForm': form})

def get_SenarioChoice(request):
	
	if request.method == 'POST':		
		R1B1 = request.POST.get('R1B1')  
		R1B2 = request.POST.get('R1B2')  
		R1B3 = request.POST.get('R1B3')  
		R2B1 = request.POST.get('R2B1')    
		R2B2 = request.POST.get('R2B2')  
		R2B3 = request.POST.get('R2B3')  
		R3B1 = request.POST.get('R3B1')  
		R3B2 = request.POST.get('R3B2')   
		R3B3 = request.POST.get('R3B3') 	
		response_data = {}      
		response_data['R1B1'] = R1B1
		response_data['R1B2'] = R1B2
		response_data['R1B3'] = R1B3
		response_data['R2B1'] = R2B1
		response_data['R2B2'] = R2B2
		response_data['R2B3'] = R2B3
		response_data['R3B1'] = R3B1
		response_data['R3B2'] = R3B2
		response_data['R3B3'] = R3B3
		form_class = office()
		form_class.R1B1 = R1B1
		form_class.R1B2 = R1B2
		form_class.R1B3 = R1B3
		form_class.R2B1 = R2B1
		form_class.R2B2 = R2B2
		form_class.R2B3 = R2B3
		form_class.R3B1 = R3B1
		form_class.R3B2 = R3B2
		form_class.R3B3 = R3B3
		form_class.save()
		
		print (connection.queries) #the SQL log
		return JsonResponse(response_data)
	else:
		form_class = officeForm()
	return render(request, 'Front.html', {'officeform': form_class})
	
