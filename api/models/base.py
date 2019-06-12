import uuid
from django.db import models

# Base model

class BaseModel(models.Model):
    """ Base model to be inherited by other models """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
       abstract = True
