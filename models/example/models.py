from django.db import models
from django.db.models import CharField


class Company(models.Model):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return f"Name: {self.name} Company: {self.company}"
