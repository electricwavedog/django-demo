# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from TestModel.models import Test


# Create your tests here.
class Tests(TestCase):
    #
    # def test_age(self):
    #     test = 11
    #     self.assertEqual(test, 11)

    def setUp(self):
        print("=======set up========")

    def test_add(self):
        # Test.objects.create(name='test', age=10, tel='13300000000')
        test = Test(name='test', age=10, tel='13300000000')
        test.save()
        # self.assertEqual(test.tel, '13300000000')
        person = Test.objects.get(name='test')
        self.assertEqual(person.tel, '13300000000')
        print("add")

    def test_find(self):
        count = Test.objects.count()
        self.assertEqual(count, 0)
        print("find")

    def tearDown(self):
        print("========tear down=========")
