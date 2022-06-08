from django.db import models


class Library(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    email =models.EmailField()
    book_name = models.CharField(max_length=30)

    def __str__(self):
        return 'Student Name :-' f" {self.fname}  {self.lname}"
