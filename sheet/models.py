from django.db import models
# from gsheets import mixins
# from uuid import uuid4

class Sheet(models.Model):
# class Sheet(mixins.SheetSyncableMixin, models.Model):

    # spreadsheet_id = '1A8OF5IHgQWSC6dnZLm8WObFCUCW8-_2SJbdcTn2SpPw'

    number = models.CharField(max_length=10)
    order_number = models.CharField(max_length=10)
    price_usd = models.CharField(max_length=10)
    delivery_time = models.CharField(max_length=10)
    price_rur = models.CharField(max_length=10)

    def __str__(self):
        return self.number
