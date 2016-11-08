# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app_user import models
from django.shortcuts import render_to_response
from django.template import Context

# Create your views here.

def insert(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.message.objects.create(username=username, password=password)
        models.message.save()
    return render_to_response('insert.html')

def list(request):
        people_list = models.message.objects.all()
        c = Context({"people_list":people_list})
        return render_to_response("showuser.html",c)
