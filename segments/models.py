from django.db import models

# Create your models here.

class Segment(models.Model):
    NEWS='News'
    ARTICLE='Article'
    PROTEST='Protest'
    DONATION='Donation'
    Type_choices=[
    (NEWS,'News'),(ARTICLE,'Article'),(PROTEST,'Protest'),(DONATION,'Donation'),
    ]
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    writeup = models.CharField(max_length=20000,default='content')
    location=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=8,choices=Type_choices, default=ARTICLE)


    def __str__(self):
        return self.summary
