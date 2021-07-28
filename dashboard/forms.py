from django import forms
from .models import InventoryItem


class PlayableCharacterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    age = forms.IntegerField(label='Age')
    description = forms.CharField(label='Description', widget=forms.Textarea)


class ItemModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.playable_character = kwargs.pop('playable_character')
        super().__init__(*args, **kwargs)

    class Meta:
        model = InventoryItem
        fields = ['name', 'number', 'description', 'weight']

    def save(self):
        inventory_item = super().save(commit=False)
        inventory_item.playable_character = self.playable_character
        inventory_item.save()

        return inventory_item

