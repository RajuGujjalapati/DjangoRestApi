from django.db import models

class Paradigm(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30)
    paradigm = models.ForeignKey(Paradigm,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Programmer(models.Model):
    name= models.CharField(max_length=30)
    languages = models.ManyToManyField(Language)
    def __str__(self):
        return self.name
class Activity(models.Model):
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    activity = models.ForeignKey(Programmer,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.start_date)
    