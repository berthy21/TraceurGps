from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70,default=None)
    password = models.CharField(max_length=100,default=None)
    groupe = models.CharField(max_length=5,default=None)



class Addresse(models.Model):
    address = models.CharField(max_length=200,null = True)

    def __str__(self) :
        return self.address


class Member(models.Model):
    membre = models.TextField(default=None)
    def __str__(self) -> str:
        return super().__str__()