from django.db import models


class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username