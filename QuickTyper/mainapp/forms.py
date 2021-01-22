from django import forms


class TextForm(forms.Form):
    text = forms.CharField(label='', max_length=100)
