from iHunterModel.models import DomainObject
from django.db import models

class Country(DomainObject):
    name = models.CharField(max_length=255, blank=False)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class State(DomainObject):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

class City(DomainObject):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

class ZipCode(DomainObject):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name