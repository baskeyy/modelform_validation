from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def inesert_topic(request):
    TF=TopicForm()
    d={'TF':TF}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('topic is inserted')
        else:
            return HttpResponse('data is not valid')
    return render(request,'insert_topic.html',d)
