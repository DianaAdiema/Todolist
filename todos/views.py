from django.shortcuts import render
from django.http import HttpResponse

from . models import Todo # to render todo items

def index(request):
	todo = Todo.object.all() [:10] # define we want 10

	context = {
	'todos':todos   # pass it onto a template variable todos
	}
	return render(request, 'index.html', context)
