from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'main'



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateField(auto_now_add=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class AuditPriceCalculator(models.Model):
    ACTIVITY_CHOICES = [
        ('servicii', 'Servicii'),
        ('producere', 'Producere'),
        ('comert', 'Comerț'),
        ('ong', 'ONG'),
        ('agricultura', 'Agricultură'),
        ('constructii', 'Construcții'),
        ('transport', 'Transport/Expediții'),
    ]

    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    sales_volume = models.FloatField(help_text="Volumul vânzărilor (mil. lei)")
    employees = models.IntegerField(help_text="Număr de salariați")
    price = models.FloatField(null=True, blank=True, help_text="Preț calculat (lei)")

    def __str__(self):
            return f"{self.activity_type} - {self.sales_volume} mil. lei - {self.employees} salariați"
    
class SolicitareServiciu(models.Model):
        nume = models.CharField(max_length=100)
        email = models.EmailField()
        telefon = models.CharField(max_length=20)
        serviciu = models.CharField(max_length=200)
        mesaj = models.TextField()
        data_trimiterii = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return f"{self.nume} - {self.serviciu}"
