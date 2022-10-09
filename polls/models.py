from django.db import models

class Manufacturer(models.Model):

    name_model = models.CharField(max_length=200)
    max_tonn = models.IntegerField(default=0)

    def __str__(self):
        return self.name_model

class Car(models.Model):

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    tonn_current = models.IntegerField(default=0)
    nomer = models.CharField(max_length=20)

    @property
    def overload_percent(self):
        return round(self.tonn_current / self.manufacturer.max_tonn*100)

    def __str__(self):
        return self.nomer

