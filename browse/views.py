from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from srd20.models import Spell, Feat, Monster

def spell_detail(request, slug):
    spell = get_object_or_404(Spell, altname=slug)
    return render_to_response('browse/spell.html',
        {
            'spell': spell,
            'editable': request.user.has_perm('srd20.change_spell'),
        },
        context_instance=RequestContext(request)
    )


def feat_detail(request, slug):
    feat = get_object_or_404(Feat, altname=slug)
    return render_to_response('browse/feat.html',
        {
            'feat': feat,
            'editable': request.user.has_perm('srd20.change_feat'),
        },
        context_instance=RequestContext(request)
    )
    
def monster_detail(request, slug):
    monster = get_object_or_404(Monster, altname=slug)
    return render_to_response('browse/monster.html',
        {
            'monster': monster,
            'editable': request.user.has_perm('srd20.change_monster'),
        },
        context_instance=RequestContext(request)
    )
    
class Favorites(TemplateView):
    template_name = "browse/favorites.html"

favorites = Favorites.as_view()
