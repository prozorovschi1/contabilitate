from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, NewsletterForm
from .models import Testimonial


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Poți salva mesajul în baza de date sau trimite-l prin email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Exemplu: Afișează un mesaj de succes
            messages.success(request, 'Mesajul tău a fost trimis cu succes! Îți mulțumim că ne-ai contactat.')
            return redirect('home')  # Redirecționează înapoi la pagina principală
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})

def home(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'home.html', {'testimonials': testimonials})


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Salvează email-ul într-o bază de date sau trimite-l unui serviciu de newsletter
            messages.success(request, 'Te-ai abonat cu succes la newsletter!')
            return redirect('home')  # Redirecționează înapoi la pagina principală
    else:
        form = NewsletterForm()

    return render(request, 'home.html', {'form': form})


def audit(request):
    return render(request, 'audit.html')

def evidenta_contabila(request):
    return render(request, 'evidenta_contabila.html')

def initierea_afacerii(request):
    return render(request, 'initierea_afacerii.html')

def consultanta_fiscala(request):
    return render(request, 'consultanta_fiscala.html')

def adresa_juridica(request):
    return render(request, 'adresa_juridica.html')

def toate_serviciile(request):
    return render(request, 'toate_serviciile.html')
