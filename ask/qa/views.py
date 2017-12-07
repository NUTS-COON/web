# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404 
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from models import Question, Answer 

from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def questions_list(request, *args, **kwargs):
    questions = Question.objects.new()
    try:
        limit = request.GET.get('limit', 10)
    except:
        limit = 10
    try:
        page = request.GET.get('page', 1)
    except:
        page = 1
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'q_list.html',
                  {'title': 'Latests',
                   'questions': page.object_list,
                   'page': page,
                   'paginator': paginator,
                   'limit': limit,
                   })


def popular(request, *args, **kwargs):
    questions = Question.objects.popular()
    try:
        limit = request.GET.get('limit', 10)
    except:
        limit = 10
    try:
        page = request.GET.get('page', 1)
    except:
        page = 1
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'q_list.html',
                  {'title': 'Popular',
                   'questions': page.object_list,
                   'page':      page,
                   'paginator': paginator,
                   'limit':     limit,
                   })


def question(request, num):
    question = get_object_or_404(Question, id=num)
    answers = question.answer_set.all()
    return render(request, 'question.html',
                  {'question': question,
                   'answers':   answers,
                  })
                 

    
