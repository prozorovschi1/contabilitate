# forms.py
from django import forms
from .models import BlogPost, AuditPriceCalculator, SolicitareServiciu


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


class AplicareForm(forms.Form):
    nume = forms.CharField(max_length=100, label="Nume Prenume")
    email = forms.EmailField(label="E-mail")
    telefon = forms.CharField(max_length=15, label="Telefon")
    
    POZITII_CHOICES = [
        ('', 'Alege poziția dorită'),
        ('contabil', 'Contabil'),
        ('auditor', 'Auditor'),
        ('consultant', 'Consultant'),
    ]
    pozitie = forms.ChoiceField(choices=POZITII_CHOICES, label="Poziție", required=True)
    
    salariu = forms.CharField(max_length=50, label="Salariul dorit", required=False)
    
    REGIUNI_CHOICES = [
        ('', 'Alege regiunea dorită'),
        ('Chisinau', 'Chișinău'),
        ('Balti', 'Bălți'),
        ('Cahul', 'Cahul'),
    ]
    regiune = forms.ChoiceField(choices=REGIUNI_CHOICES, label="Regiune", required=True)
    
    cv = forms.FileField(label="Atașează CV-ul tău")

class SolicitareServiciuForm(forms.ModelForm):
    class Meta:
        model = SolicitareServiciu
        fields = ['nume', 'email', 'telefon', 'serviciu', 'mesaj']