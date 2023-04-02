from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("subject","email", "sender", "detail")

        widgets = {
            'subject': forms.TextInput(attrs={
            'class': 'form-control col-md-4'
            }),
            'email': forms.EmailInput(attrs={
            'class': 'form-control col-md-4'
            }),
            'sender': forms.TextInput(attrs={
            'class': 'form-control col-md-4'
            }),
            'detail': forms.Textarea(attrs={
            'class': 'form-control col-md-4'
            })
        }
