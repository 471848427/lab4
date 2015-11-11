from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Country = models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s' %self.Name
        
class Book(models.Model):
    ISBN = models.IntegerField(primary_key = True)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=50)
    PublishDate = models.DateField()
    Price = models.DecimalField(decimal_places=2,max_digits=4)
    def __unicode__(self):
        return u'%s' %self.Title
