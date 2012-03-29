from django import template
from django.core.urlresolvers import reverse

from favorites.models import FavoriteFeat

register = template.Library()

@register.inclusion_tag('favorites/label_as_favorite.html', takes_context=True)
def favorite_feat(context, feat):
    user = context['user']
    is_favorite = FavoriteFeat.objects.filter(feat=feat, user=user).exists()
    return {
        'is_favorite': is_favorite,
        'favorite_url': reverse('favorite_feat', kwargs={'slug': feat.altname}),
        'unfavorite_url': reverse('unfavorite_feat', kwargs={'slug': feat.altname}),
    }
