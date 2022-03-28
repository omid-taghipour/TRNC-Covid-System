from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    student = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    passport = models.CharField(max_length=15)

    def __str__(self):
        return self.student.first_name + " "+self.student.last_name


class Covid_Test(models.Model):
    student = models.OneToOneField(Profile, related_name='student_test', on_delete=models.CASCADE)
    barcode = models.CharField(max_length=12, blank=False)
    result = models.CharField(max_length=8)
    date_time = models.DateTimeField(blank=False)

    def __str__(self):
        return str(self.student.id) + " - " + self.barcode
