from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CertificateData(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    full_name = models.CharField("Name", max_length=30, null=False)
    relation = models.CharField("Relation", max_length=30, null=False)
    tag_line = models.CharField("Tag Line", max_length=100, null=False)
    resiver = models.CharField("Resiver", max_length=30, null=False)
    date = models.DateField('Date', auto_now_add=True)

    def __str__(self):
        return self.full_name
