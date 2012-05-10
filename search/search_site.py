from django_search_views.search import SearchCategory, Search

from srd20.models import Spell, Feat, Monster

# These are the fields searched by the full text search
SEARCH_FIELDS = (
    'name',
    'altname',
    'short_description',
    'description',
    'school',
    'subschool',
    'descriptor',
    'material_components',
    'reference',
)


class SpellByName(SearchCategory):
    model = Spell    
    lookups = ['name__icontains']
    def verbose_name(self): return u'spells'

class SpellFullText(SearchCategory):
    model = Spell    
    lookups = [field+'__icontains' for field in SEARCH_FIELDS]
    def verbose_name(self): return u'spells (full text)'

class FeatByName(SearchCategory):
    model = Feat    
    lookups = ['name__icontains']
    def verbose_name(self): return u'feats'

class MonsterByName(SearchCategory):
    model = Monster    
    lookups = ['name__icontains']
    def verbose_name(self): return u'monsters'

class SiteSearch(Search):
    categories = [SpellByName, SpellFullText, FeatByName, MonsterByName]

site = SiteSearch()
urls = site.urls()

