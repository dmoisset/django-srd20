from django.http import Http404
from django.template.response import TemplateResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from srd20.models import Spell, Feat
from favorites.models import FavoriteSpell, FavoriteFeat

@login_required
def flag_as_favorite_feat(request, slug):
    if request.method != 'POST':
        raise Http404
    feat = get_object_or_404(Feat, altname=slug)
    FavoriteFeat.objects.get_or_create(user=request.user, feat=feat)
    return redirect(feat.get_absolute_url())

@login_required
def unfavorite_feat(request, slug):
    if request.method != 'POST':
        raise Http404
    feat = get_object_or_404(Feat, altname=slug)
    FavoriteFeat.objects.filter(user=request.user, feat=feat).delete()
    return redirect(feat.get_absolute_url())

@login_required
def favorite_lists(request):
    feats = Feat.objects.filter(favoritefeat__user=request.user)
    return TemplateResponse(request, 'favorites/list.html', {'feats': feats})

