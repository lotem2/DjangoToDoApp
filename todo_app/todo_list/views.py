from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	if request.method == 'POST':
		
		form = ListForm(request.POST or none)

		if form.is_valid():
			form.save()
			messages.success(request, "Item has been added successfully to the list!")
			
			#all_items = List.objects.all
		
	#else: # if we did not enter if it's a GET request
	all_items = List.objects.all  # get all objects from the List	
	return render(request, 'home.html', {'all_items': all_items})

def about(request):	
	context = {'first_name': "Lotem", 'last_name': "Leder"}
	return render(request, 'about.html',context)

def delete(request, list_id):
	item = List.objects.get(pk = list_id)
	item.delete()
	messages.success(request, "Item has been deleted successfully!")
	return redirect('home')

def cross_off(request, list_id):
	item = List.objects.get(pk = list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request, list_id):
	item = List.objects.get(pk = list_id)
	item.completed = False
	item.save()
	return redirect('home')

def edit(request, list_id):
	item = List.objects.get(pk=list_id)

	if request.method == 'POST':
		
		form = ListForm(request.POST or none, instance = item)

		if form.is_valid():
			form.save()
			messages.success(request, "Item has been added edited successfully!")
			return redirect('home')
			
			
	item = List.objects.get(pk=list_id)  # get all objects from the List	
	return render(request, 'edit.html', {'item': item})


