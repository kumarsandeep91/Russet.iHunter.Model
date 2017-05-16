from iHunterModel.models import DomainObject
from django.db import models

# title or designation
class Title(DomainObject):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name