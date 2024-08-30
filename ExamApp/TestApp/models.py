from django.db import models

class Candidate(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(null=False, max_length=20)
    name = models.CharField(null=False, max_length=30)
    test_attmpted = models.IntegerField()
    points=models.FloatField()

    def __str__(self) -> str:
        return self.username

class Question(models.Model):
    qid = models.BigAutoField(primary_key=True, auto_created=True)
    que = models.TextField()
    a = models.CharField(max_length=250)
    b = models.CharField(max_length=250)
    c = models.CharField(max_length=250)
    d = models.CharField(max_length=250)
    ans = models.CharField(max_length=250)

class Result(models.Model):
    resultid = models.BigAutoField(primary_key=True, auto_created=True)
    username = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attempt=models.IntegerField()
    right = models.IntegerField()
    wrong = models.IntegerField() 
    point = models.FloatField()   


# Create your models here.