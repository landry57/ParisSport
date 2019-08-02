from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=120)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Compte(models.Model):
    sold = models.IntegerField(default=0)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.sold

class Paris(models.Model):
    vs = models.CharField(max_length=120)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.vs

    class Meta:
        ordering = ('vs',)
