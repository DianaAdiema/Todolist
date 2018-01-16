from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo # to render todo items

def index(request):
	todos = Todo.objects.all() [:10] # define we want 10

	context = {
	'todos':todos   # pass it onto a template variable todos
	}
	return render(request, 'index.html', context)

def details(request, id):
	todo=Todo.objects.get(id='id')
	context = {
	'todo':todo   # pass it onto a template variable todos
	}
	return render(request, 'details.html', context)
