from django.db import models

# Create your models here.
class IssuedBook(models.Model):
    student_roll_number=models.CharField(max_length=50)
    library_card_number=models.CharField(max_length=50)
    book_title=models.CharField(max_length=100)
    author_name=models.CharField(max_length=200)
    issue_date=models.DateField