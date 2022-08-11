from django.db import models


class Contact(models.Model):
    name = models.CharField(default='', max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(default='', max_length=200)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
