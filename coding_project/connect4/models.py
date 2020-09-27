from django.db import models
import uuid


class GameBoard(models.Model):
    token = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False, unique=True)
    datetime = models.DateTimeField(auto_now=True)
    all_moves = models.CharField(default = '{}', max_length=1000000)
    move_num = models.IntegerField(default=0)
    row1 = models.IntegerField(default=999999999)
    row2 = models.IntegerField(default=999999999)
    row3 = models.IntegerField(default=999999999)
    row4 = models.IntegerField(default=999999999)
    row5 = models.IntegerField(default=999999999)
    row6 = models.IntegerField(default=999999999)

    def __str__(self):
        return str(self.token)

