from django import forms

class Search(forms.Form):
    searchText = forms.CharField(max_length=100)