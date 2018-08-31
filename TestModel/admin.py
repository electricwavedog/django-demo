# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from TestModel.models import Test, Test2

# Register your models here.


class Test2Admin(admin.TabularInline):
    model = Test2

    extra = 3


class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'tel']

    search_fields = ['name']

    fields = ['name', 'tel']

    list_filter = ['name']

    inlines = [Test2Admin]


admin.site.register(Test, TestAdmin)
admin.site.register(Test2)
