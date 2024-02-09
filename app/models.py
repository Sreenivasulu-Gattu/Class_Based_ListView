from django.db import models

# Create your models here.

class School(models.Model):
    sname = models.CharField(max_length = 100)
    sprinc = models.CharField(max_length = 100)
    sloc = models.CharField(max_length = 100)

    def __str__(self):
        return self.sname

class Student(models.Model):
    stdname = models.CharField(max_length = 100)
    stdage = models.IntegerField()
    sname = models.ForeignKey(School,on_delete = models.CASCADE,related_name = 'student')