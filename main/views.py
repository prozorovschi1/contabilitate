from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from .forms import ContactForm, NewsletterForm, AuditPriceForm, AplicareForm
from .models import Testimonial, BlogPost
from .utils import calculate_audit_price
from django.core.mail import EmailMessage
from .forms import SolicitareServiciuForm


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
    form = AuditPriceForm()
    calculated_price = None

    if request.method == 'POST':
        form = AuditPriceForm(request.POST)
        if form.is_valid():
            sales_volume = form.cleaned_data['sales_volume']
            activity_type = form.cleaned_data['activity_type']
            employees = form.cleaned_data['employees']

            calculated_price = calculate_audit_price(sales_volume, activity_type, employees)

    context = {
        'form': form,
        'calculated_price': calculated_price,
    }
    
    return render(request, 'audit.html', context)

def evidenta_contabila(request):
    if request.method == "POST":
        form = SolicitareServiciuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Solicitarea a fost trimisă cu succes!")
            return redirect('evidenta_contabila')
        else:
            messages.error(request, "A apărut o eroare. Verifică datele introduse.")
    else:
        form = SolicitareServiciuForm(request.POST)

    return render(request, 'evidenta_contabila.html', {'form': form})

def initierea_afacerii(request):
    return render(request, 'initierea_afacerii.html')

def consultanta_fiscala(request):
    return render(request, 'consultanta_fiscala.html')

def adresa_juridica(request):
    return render(request, 'adresa_juridica.html')

def toate_serviciile(request):
    return render(request, 'toate_serviciile.html')

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog_detail.html', {'post': post})

def cariera_view(request):
    if request.method == 'POST':
        form = AplicareForm(request.POST, request.FILES)
        if form.is_valid():
            # Obține datele din formular
            nume = form.cleaned_data['nume']
            email = form.cleaned_data['email']
            telefon = form.cleaned_data['telefon']
            pozitie = form.cleaned_data['pozitie']
            salariu = form.cleaned_data['salariu']
            regiune = form.cleaned_data['regiune']
            cv = request.FILES['cv']

            # Trimite email cu datele aplicantului
            mesaj = f"""
            Aplicare nouă pentru poziția {pozitie}:

            Nume Prenume: {nume}
            E-mail: {email}
            Telefon: {telefon}
            Salariul dorit: {salariu}
            Regiune: {regiune}
            """
            email_mesaj = EmailMessage(
                subject=f"Aplicare nouă: {pozitie}",
                body=mesaj,
                from_email="noreply@firma-ta.com",
                to=["hr@firma-ta.com"],
            )
            email_mesaj.attach(cv.name, cv.read(), cv.content_type)
            email_mesaj.send()

            messages.success(request, "Aplicarea a fost trimisă cu succes!")
            form = AplicareForm()  # Resetează formularul după trimitere
        else:
            messages.error(request, "Te rugăm să completezi corect toate câmpurile.")
    else:
        form = AplicareForm()

    return render(request, 'cariera.html', {'form': form})