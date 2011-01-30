from django import forms

class SearchForm(forms.Form):
    SEARCH_TYPES = (
        ('name', 'By Title'),
        ('all', 'Full Text Search')
    )

    q = forms.CharField(label='Search', max_length=64)
    search_type = forms.ChoiceField(choices=SEARCH_TYPES, widget=forms.RadioSelect, initial='name')
    
