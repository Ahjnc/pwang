from django.db import models
from django.contrib import admin
import sys
# Create your models here.
reload(sys)   
sys.setdefaultencoding('utf8')
class Author(models.Model):
    AuthorID = models.CharField(primary_key=True,max_length = 10)
    Name = models.CharField(max_length = 10)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 10)

    def __unicode__(self):
	return self.Name
class Book(models.Model):
    ISBN = models.CharField(primary_key=True,max_length = 10)
    Title = models.CharField(max_length = 150)
    AuthorID = models.ForeignKey(Author,related_name='AutorID_Book')
    Publisher = models.CharField(max_length = 20)
    PublishDate = models.TextField()
    Price = models.IntegerField()

    def __unicode__(self):
	return str(self.Title)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('AuthorID','Name','Age','Country')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book)
