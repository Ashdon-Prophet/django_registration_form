#  Inside apps/first_app/views.py
from django.shortcuts import render, redirect
from datetime import datetime
import random
# Create your views here.
def index(request):
    print ('***\n')*5
    print "...index..."
    print ('***\n')*5
    return render(request, 'first_app/index.html')
#end def
def create(request):
    print ('***\n')*5
    print "...create..."
    print ('***\n')*5
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')
#end def
def result(request):
    print ('***\n')*5
    print "...result..."
    print ('***\n')*5
    return render(request, 'first_app/result.html')
#end def
