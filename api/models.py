from django.db import models
from django.contrib.auth.models import User
import uuid


class SitePassword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    url = models.CharField(max_length=1024, db_index=True)
    password = models.CharField(max_length=1024)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(null=True, default=None)
