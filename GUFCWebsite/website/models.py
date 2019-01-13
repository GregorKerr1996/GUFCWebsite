from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length = 128, unique = True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.name

class MatchReport(models.Model):
    name = models.CharField(max_length = 128, unique = True)

    def __str__(self):
        return self.name

class Report(models.Model):
    matchReport = models.ForeignKey(MatchReport)
    title = models.CharField(max_length = 128)
    #date = models.DateField()
    text = models.TextField()
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
