from django.db import models

class Document(models.Model):
    docName = models.CharField(max_length=60)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Mails(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=20000)
    def __str__(self):
        return self.email 
