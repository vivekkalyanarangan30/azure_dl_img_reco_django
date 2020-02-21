# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Image(models.Model):
    #img_id = models.BigIntegerField(default=10)
    img = models.ImageField(upload_to='upload_img/')
    house = models.FloatField(default=0.0)
    blueprint = models.FloatField(default=0.0)
    others = models.FloatField(default=0.0)
    created_dt_tm = models.DateTimeField(auto_now=True)