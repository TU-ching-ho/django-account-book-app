from django.db import models

# Create your models here.


class Expense(models.Model):
    name = models.CharField(max_length=255)  # 花費項目
    price = models.IntegerField()  # 金額
