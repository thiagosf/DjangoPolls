from django import forms

class GalleryForm(forms.Form):
    image = forms.ImageField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
