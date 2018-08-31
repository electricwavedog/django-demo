# -*- coding: utf-8 -*-

from TestModel.models import Test
from django.forms.models import model_to_dict
from django.db import connection, transaction


def find(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TestModel_test WHERE id=%s", [id])
    print dictfetchall(cursor)
    info = Test.objects.get(id=id)
    return model_to_dict(info)


@transaction.atomic
def update(id, name, age, tel):
    Test.objects.filter(id=id).update(name=name, age=age, tel=tel)


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
