from django.db import models

# Create your models here.


class Powerball(models.Model):
    date_drawing = models.DateField(blank=True, null=True)
    ball_1 = models.IntegerField(blank=True, null=True)
    ball_2 = models.IntegerField(blank=True, null=True)
    ball_3 = models.IntegerField(blank=True, null=True)
    ball_4 = models.IntegerField(blank=True, null=True)
    ball_5 = models.IntegerField(blank=True, null=True)
    powerball = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.date_drawing)

    class Meta:
        managed = False
        db_table = 'powerball'