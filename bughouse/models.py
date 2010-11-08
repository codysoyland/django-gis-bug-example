from django.db import models

class Bug(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()

    def __unicode__(self):
        return self.name

class Patch(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    bugs = models.ForeignKey(Bug, related_name='patches')

    def __unicode__(self):
        return self.name
