from enum import auto
from django.db import models
from Users.models import MyUser

# Create the Bet object


class Bets(models.Model):
    username = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE
    )
    posted_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.body
