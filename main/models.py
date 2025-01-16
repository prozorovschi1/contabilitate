from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'main'