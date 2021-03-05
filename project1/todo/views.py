from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import *


# View showing every item in todo list
class IndexView(generic.ListView):
	template_name = 'todo/index.html'
	context_object_name = 'todo_list'

	def get_queryset(self):
		return Todo.objects.all()


def addItem(request):
	time = timezone.now()
	content = request.POST["todo-content"]

	Todo.objects.create(todo_text=content, added_date=time)
	return HttpResponseRedirect(reverse('todo:index'))
