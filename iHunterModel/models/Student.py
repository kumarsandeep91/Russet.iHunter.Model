from iHunterModel.models import Person
from django.db import models

# student class
class Student(Person):
    roll = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.first_name