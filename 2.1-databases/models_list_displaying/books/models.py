# coding=utf-8
from django.db import models
from pytils.translit import slugify


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    image = models.URLField(u'Обложка', blank=True, null=True)
    pub_date = models.DateField(u'Дата публикации')
    slug = models.SlugField(u'slug', allow_unicode=True, null=True, unique=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Books, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name + " " + self.author            
