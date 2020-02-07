from django.db import models
from .library import Library
from .librarian import Librarian

class Book (models.Model):

    title = models.CharField(max_length=50)
    ISBN_number = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

