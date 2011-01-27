from django.shortcuts import get_object_or_404, render_to_response
from srd20.models import Spell

def spell_detail(request, id):
    spell = get_object_or_404(Spell, pk=id)
    return render_to_response('browse/spell.html', {'spell': spell})

