from django.db import models

class UserBase(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Client(UserBase):
    address = models.CharField(max_length=255)

class Employee(UserBase):
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField()

class Admin(UserBase):
    role = models.CharField(max_length=50)