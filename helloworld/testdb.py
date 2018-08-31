# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
    # test = Test(name='aaa')
    # test.save()
    # response = ""
    # list = Test.objects.order_by("id")
    # for var in list:
    #     response += var.name + " "
    test = Test.objects.get(id=1)
    test.name = "aab"
    test.save()

    Test.objects.filter(id=2).update(name="bbc")
    return HttpResponse("<p>success</p>")
