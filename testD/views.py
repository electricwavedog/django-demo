# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import testdb
from django.views.decorators import csrf
from django.http import HttpResponse
# from django.template import RequestContext, loader

# Create your views here.


def toPage(request):
    id = 1
    info = testdb.find(id)
    # info = {"name": "aaa", "tel": "123", "age": "20"}
    context = {'info': info}
    return render(request, "test.html", context)


def update(request):
    id = 1
    if request.POST:
        testdb.update(id, request.POST["name"], request.POST["age"], request.POST["tel"])
    return HttpResponse("update success")
