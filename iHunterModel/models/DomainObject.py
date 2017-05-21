import uuid
from django.db import models

# abstract base class for all domain objects.
class DomainObject(models.Model):
    """The base class for every model. This class contains **id(Primary Key)** for every model."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True