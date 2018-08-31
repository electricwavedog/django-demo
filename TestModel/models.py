# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField('用户名', max_length=20)
    age = models.IntegerField('年龄', null=True)
    tel = models.CharField('电话', max_length=11, null=True)

    def __unicode__(self):
        return self.name


class Test2(models.Model):
    name = models.CharField('test', max_length=20)
    foreignId = models.ForeignKey(Test)

    def __unicode__(self):
        return self.name
