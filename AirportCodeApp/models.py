from django.db import models

class AirportCodes(models.Model):
    City = models.CharField(max_length=200)
    Airport_Code = models.CharField(max_length=4)

#   def __str__(self):
#       return self.City + ' | ' + str(self.Airport_Code)

