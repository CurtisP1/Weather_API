#  Copyright (c) 2023 - All rights reserved.
#  Created by Curtis Poon for PROCTECH 4IT3/SEP 6IT3.
#  SoA Notice: I Curtis Poon, 400263978 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.db import models


class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username
