from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.ForeignKey('Gender', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Gender(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)