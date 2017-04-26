import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class JobPosition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, default='Programmer')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    #position = GenericRelation(JobPosition)
    position = models.ForeignKey(JobPosition, related_name='jobposition', on_delete=models.CASCADE)
    is_working = models.BooleanField(default=False)

    class Meta:
        # unique_together = ('jobposition', 'created')
        ordering = ['created']

    def __str__(self):
        return self.first_name
