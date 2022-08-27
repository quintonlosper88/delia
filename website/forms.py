from email.message import Message
from socket import fromshare
from django import forms
from .models import Messages

class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = {
            'first_name',
            'last_name',
            'phone',
            'email',
            'message'
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class' : 'form-control mb-30', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control mb-30', 'placeholder':'Last Name'}),
            'phone': forms.TextInput(attrs={'class' : 'form-control mb-30', 'placeholder':'Phone Number (+27)', 'type':'phone'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control mb-30', 'placeholder':'email','type':'Email'}),
            'message': forms.Textarea(attrs={'class' : 'form-control mb-30', 'placeholder':'Start Discussion'})
        }
