from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class State(models.Model):
    state_name = models.CharField(max_length=200)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=200)
    state_name = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    parent_id = models.IntegerField(default=0)

    def __str__(self):
        return self.category_name


class Biz(models.Model):
    year=[("2019","2019"),("2018","2018")]
    biz_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,blank=True)
    primary_contact=models.IntegerField()
    secondary_contact=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    logo=models.ImageField(upload_to="biz/")
    website=models.URLField()
    estd_year=models.CharField(max_length=200,choices=year)
    doc=models.DateTimeField(default=timezone.now)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Biz, self).save(*args,**kwargs)

    def __str__(self):
        return self.title
