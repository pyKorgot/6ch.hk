from django import forms


class MessageForms(forms.Form):
    message = forms.CharField(max_length=500, widget=forms.Textarea)
