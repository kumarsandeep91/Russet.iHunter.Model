import uuid
from django.db import models

# abstract base class for all domain objects.
class DomainObject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True