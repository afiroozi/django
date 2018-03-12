from django.db import models


class News(models.Model):
    head = models.CharField(max_length=100, default=None, blank=True, null=True)
    body = models.TextField(default=None, blank=True, null=True)
    insertTime = models.TimeField(default=None, blank=True, null=True)
    insertDate = models.DateField(default=None, blank=True, null=True)
    today = models.DateTimeField(default=None, blank=True, null=True)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.head
