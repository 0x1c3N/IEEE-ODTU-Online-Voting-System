from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    is_active = models.BooleanField(default=True)
    totalvote = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    birinci = models.CharField(max_length=200,null=True,blank = True)
    ikinci = models.CharField(max_length=200,null=True,blank = True)
    ucuncu = models.CharField(max_length=200,null=True,blank = True)
    dorduncu = models.CharField(max_length=200,null=True,blank = True)
    besinci = models.CharField(max_length=200,null=True,blank = True)
    altinci = models.CharField(max_length=200,null=True,blank = True)
    yedinci = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to='../staticfiles/',null=True,blank = True)
    imagename = models.CharField(max_length=200,null=True,blank=True)
    votes = models.IntegerField(default=0)
    negativevotes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        return self.image
        return self.ikinci

class Voter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
