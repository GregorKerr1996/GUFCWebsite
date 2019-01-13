from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    views = models.IntegerField(default = 0)
    slug = models.SlugField(unique = True)

    class Meta:
        verbose_name_plural = "News"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Report(models.Model):
    news_cat = models.ForeignKey(News)
    title = models.CharField(max_length = 128)
    #date = models.DateField()
    text = models.TextField()
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.title