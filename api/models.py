from django.db import models


class Transaction(models.Model):
    hash = models.CharField(max_length=80)
    block_number = models.IntegerField()
    from_address = models.CharField(max_length=48)
    to_address = models.CharField(max_length=48)
    quantity = models.CharField(max_length=80)
    timestamp = models.IntegerField()
    input_data = models.TextField()

    def __str___(self):
        return "block: %s transaction: %s from: %s to: %s quantity: %s timestamp: %s input: %s" % (
            self.block_number, self.hash, self.from_address, self.to_address, self.quantity, self.timestamp, self.input_data)
