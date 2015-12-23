from django.db import models

from django.db import models

class ClientQuery(models.Model):
    query_text = models.CharField(max_length=2000)
    sender = models.CharField(max_length=200)
