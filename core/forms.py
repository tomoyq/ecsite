from django import forms

from .models import Category

class SerchForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects, label='カテゴリ', empty_label='選択してください')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'forrm-select'})

    