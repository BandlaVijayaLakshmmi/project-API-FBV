from django.db import models

# Create your models here.
class Employee(models.Model):
    Ename=models.CharField(max_length=100,primary_key=True)
    Eage=models.IntegerField()
    Ephno=models.IntegerField()
    def __str__(self):
        return self.Ename