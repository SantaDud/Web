from django.core.files import storage
from django.db import models
from django.db.models.fields import CharField, EmailField, TextField
from django.db.models.fields.files import FileField, ImageField
from django.core.files.storage import FileSystemStorage
from django.db.models.fields.related import ManyToManyField
# Create your models here.

fileStorage = FileSystemStorage(location='libr/')

class Book(models.Model):
    title = CharField(max_length=50)
    author = CharField(max_length=30)
    cover = ImageField(storage=fileStorage, upload_to='static/libr/pictures')
    description = TextField()
    ISBN = CharField(max_length=14)
    bookPDF = FileField(storage=fileStorage, upload_to='static/libr/pdf')
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class User(models.Model):
    fname = CharField(max_length=30)
    lname = CharField(max_length=30)
    username = CharField(max_length=30)
    email = EmailField(max_length=50)
    password = CharField(max_length=15)
    favorites = ManyToManyField("Book")
    def __str__(self):
        return f'{self.fname} {self.lname} ({self.email})'
