# Create your views here.
from django.shortcuts import render_to_response
from .forms import SearchForm
from srd20.models import Spell

def search_start(request):
    return render_to_response('search/start.html', {'form': SearchForm()})

def search_results(request):
    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            results = Spell.objects.filter(name__icontains=form.cleaned_data['q'])
    else:
        form = SearchForm()
        results = None
    return render_to_response('search/results.html', {'form': form, 'results': results})
