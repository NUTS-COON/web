# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(blank = True, null = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name = 'question_like_user')

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add = True)
    question = models.ForeignKey(Question, null = True, on_delete = models.SET_NULL)
    author = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)

    def __unicode__(self):
        return self.text


