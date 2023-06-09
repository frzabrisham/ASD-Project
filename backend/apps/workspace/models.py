import uuid
from datetime import datetime, timedelta


from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    title = models.CharField(unique=True, max_length=100)
    color = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null=True)
    users = models.ManyToManyField(to=User, related_name='boards')


class CardsList(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class Card(models.Model):
    card_list = models.ForeignKey(CardsList, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    description = models.CharField(max_length=10000, default=None, null=True)
    due_date = models.DateTimeField(default=None, null=True)



class JoinRequest(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    token = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)

    @staticmethod
    def get_unique_token():
        for i in range(10):
            token = uuid.uuid1()
            if not JoinRequest.objects.filter(token=token).exists():
                return token
                break
        else:
            raise Exception("Cannot Save Model!")
