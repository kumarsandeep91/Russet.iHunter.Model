from iHunterModel.models import DomainObject
from django.db import models

class Standard(DomainObject):
    name = models.CharField(max_length=255, null=False, blank=False) 

    def __str__(self):
        return self.name