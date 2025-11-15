from djangi.db import models

class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    has_delivery=models.BooleanField(default=False)

    def __str__(self):
        return self.name