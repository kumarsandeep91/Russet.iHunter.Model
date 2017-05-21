from iHunterModel.models import DomainObject, Address
from django.db import models

class ContactType(DomainObject):
    # required field. values may contain 9857658888, xxxxx@xxxx.com etc
    name = models.CharField(max_length=255, blank=False)

class Contact(DomainObject):
    # required field. values may contain 9857658888, xxxxx@xxxx.com etc
    name = models.CharField(max_length=255, blank=False)

    # relationships.
    # each contact have one contact type i.e phone, fax, email etc
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE, blank=False, null=False) # required
    # a address can have multiple contacts
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)