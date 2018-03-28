from django.shortcuts import render, redirect
from django.http import HttpResponse
from snippets.forms import SnippetForm
from snippets.models import Snippet

def create(request):
	if request.method == "GET":
		form = SnippetForm()
	elif request.method == "POST":
		form = SnippetForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			snippet = Snippet(title=data.get('title'), content=data.get('content'))
			snippet.save()
		return redirect('view', snippet.id)
	return render(request, 'snippets/create.html', {'form': form})

def view(request, key):
	return HttpResponse("View Function: " + str(key))
