from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class List_today(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class List_thisweek(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class List_thismonth(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class List_spare_time(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)