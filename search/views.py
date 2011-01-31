# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import Q
from .forms import SearchForm
from srd20.models import Spell

def search_start(request):
    return render_to_response('search/start.html', {'form': SearchForm()})

# These are the fields searched by the full text search
SEARCH_FIELDS = (
    'altname',
    'short_description',
    'description',
    'school',
    'subschool',
    'descriptor',
    'material_components',
    'reference',
)

def search_results(request):
    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query_string = form.cleaned_data['q']
            query = Q(name__icontains=query_string)
            if form.cleaned_data['search_type'] == 'all':
                for field in SEARCH_FIELDS:
                    query |= Q(**{field+'__icontains': query_string})
            results = Spell.objects.filter(query)
    else:
        form = SearchForm()
        results = None
    return render_to_response('search/results.html', {'form': form, 'results': results})
