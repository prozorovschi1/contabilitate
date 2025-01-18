from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('audit/', views.audit, name='audit'),
    path('evidenta-contabila/', views.evidenta_contabila, name='evidenta_contabila'),
    path('initierea-afacerii/', views.initierea_afacerii, name='initierea_afacerii'),
    path('consultanta-fiscala/', views.consultanta_fiscala, name='consultanta_fiscala'),
    path('adresa-juridica/', views.adresa_juridica, name='adresa_juridica'),
    path('toate-serviciile/', views.toate_serviciile, name='toate_serviciile'),

    path('blog/', views.blog_list, name='blog_list'),
]
