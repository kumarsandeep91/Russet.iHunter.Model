from iHunterModel.models import DomainObject
from django.db import models

class Country(DomainObject):
    name = models.CharField(max_length=255, blank=False)

class State(DomainObject):
    name = models.CharField(max_length=255, blank=False)

class City(DomainObject):
    name = models.CharField(max_length=255, blank=False)

class ZipCode(DomainObject):
    name = models.CharField(max_length=255, blank=False)

