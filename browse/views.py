from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from srd20.models import Spell
from srd20.models import FeatType
from srd20.models import Feat

def spell_detail(request, id):
    spell = get_object_or_404(Spell, pk=id)
    return render_to_response('browse/spell.html',
        {
            'spell': spell,
            'editable': request.user.has_perm('srd20.can_edit_spell'),
        },
        context_instance=RequestContext(request)
    )


def feat_type_detail(request, id):
    feat_type = get_object_or_404(FeatType, pk=id)
    return render_to_response('browse/feat_type.html',
        {
            'feat_type': feat_type,
            'editable': request.user.has_perm('srd20.can_edit_feat_type'),
        },
        context_instance=RequestContext(request)
    )


def feat_detail(request, id):
    feat = get_object_or_404(Feat, pk=id)
    return render_to_response('browse/feat.html',
        {
            'feat': feat,
            'editable': request.user.has_perm('srd20.can_edit_feat'),
        },
        context_instance=RequestContext(request)
    )
