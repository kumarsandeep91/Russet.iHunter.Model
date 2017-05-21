from iHunterModel.models import DomainObject, Organization, Country, State, City, ZipCode
from django.db import models

class Address(DomainObject):
    # name/type of address i.e home, office etc.
    name = models.CharField(max_length=255, blank=False)
    address_line1 = models.CharField(max_length=255, blank=False)
    address_line2 = models.CharField(max_length=255, blank=True)

    # relationships
    # each address can be blong to only one country
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    zipcode = models.ForeignKey(ZipCode, on_delete=models.CASCADE, blank=True, null=True)

    # a organization can have many addresses.
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)