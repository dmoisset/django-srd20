# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import Q
from django.template import RequestContext
from .forms import SearchForm
from srd20.models import Spell

def search_start(request):
    return render_to_response('search/start.html',
        {'form': SearchForm()},
        context_instance=RequestContext(request))

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
    results = None # default if no results are produced
    query_string= None
    if 'q' in request.GET: # This is a get form, so we use this to decide whether we want a bounded or unbounded form
        form = SearchForm(request.GET)
        if form.is_valid():
            query_string = form.cleaned_data['q']
            # Always search by name
            query = Q(name__icontains=query_string)
            # when full text requested, add fields to the query
            if form.cleaned_data['search_type'] == 'all':
                for field in SEARCH_FIELDS:
                    query |= Q(**{field+'__icontains': query_string})
            results = Spell.objects.filter(query)
    else:
        # No query. Assuming this is not the result of submitting
        form = SearchForm()
    return render_to_response('search/results.html', {
            'form': form,
            'results': results,
            'query': query_string
        },
        context_instance=RequestContext(request)
    )
