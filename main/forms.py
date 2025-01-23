# forms.py
from django import forms
from .models import BlogPost, AuditPriceCalculator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nume")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Mesaj")


class NewsletterForm(forms.Form):
    email = forms.EmailField(label="Email")



class AuditPriceForm(forms.ModelForm):
    class Meta:
        model = AuditPriceCalculator
        fields = ['sales_volume', 'activity_type', 'employees']
        widgets = {
            'sales_volume': forms.NumberInput(attrs={'class': 'form-control'}),
            'activity_type': forms.Select(attrs={'class': 'form-control'}),
            'employees': forms.NumberInput(attrs={'class': 'form-control'}),
        }
