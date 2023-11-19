from django.contrib import admin
from django.db import models

from hello.models import Gender, Person

admin.site.register(Person)
admin.site.register(Gender)
