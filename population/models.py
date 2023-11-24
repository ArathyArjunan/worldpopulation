from django.db import models

class Worldpopulation(models.Model):
    place=models.PositiveIntegerField()
    pop1980=models.PositiveIntegerField()
    pop2000=models.PositiveIntegerField()
    pop2010=models.PositiveIntegerField()
    pop2022=models.PositiveIntegerField()
    pop2023=models.PositiveIntegerField()
    pop2030=models.PositiveIntegerField()
    pop2050=models.PositiveIntegerField()
    country=models.CharField(max_length=200,unique=True)
    area=models.PositiveIntegerField()
    landAreaKm=models.FloatField()
    cca2=models.CharField(max_length=200)
    cca3=models.CharField(max_length=200)
    netChange=models.FloatField()
    growthRate=models.FloatField()
    worldPercentage=models.FloatField()
    density=models.FloatField()
    densityMi=models.FloatField()
    rank=models.PositiveIntegerField()
    


    def __str__(self) :
        return self.country