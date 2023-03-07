from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    title = models.CharField(unique=True, max_length=100)
    color = models.CharField(max_length=50)
    privacy = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null=True)

    def to_dict(self):
        return {
            "title": self.title,
            "color": self.color,
            "privacy": self.privacy
        }


class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    order = models.IntegerField()


class Card(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, default=None)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }


class BoardFollowing(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)