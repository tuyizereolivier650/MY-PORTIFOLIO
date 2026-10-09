from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email address", "class": "form-control"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Write your message here...", "class": "form-control form-textarea", "rows": 6}),
        }
        labels = {
            "name": "Name",
            "email": "Email",
            "subject": "Subject",
            "message": "Message",
        }
