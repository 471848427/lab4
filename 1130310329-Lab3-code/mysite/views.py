# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 12:31:16 2015

@author: Magics
"""

from django.shortcuts import render_to_response,HttpResponse
from books.models import Book,Author
from django.template import RequestContext


def home(request):
    return render_to_response('homepage.html')
    
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:          
            try:            
                author = Author.objects.get(Name=q)
                Books = Book.objects.filter(AuthorID=author)                
                return render_to_response('search_results.html',{'book':Books,'query':q})
            except:
                return render_to_response('search_results.html')
    return render_to_response('search_form.html',{'error':error})

    
def display(request,offset):
    offset = int(offset)
    books = Book.objects.get(ISBN=offset)
    authors = books.AuthorID
    return render_to_response('display.html',{'book':books,'author':authors})
    
def dele(request,offset):
    offset = int(offset)
    Book.objects.get(ISBN=offset).delete()
    return render_to_response('deleted.html')
        
def addnew(request):
    if request.method == "GET":
        return render_to_response('add_new.html',context_instance=RequestContext(request))
    request.session['i'] = request.POST.get('isbn')
    request.session['t'] = request.POST.get('title')
    author1 = request.POST.get('author')
    request.session['p'] = request.POST.get('publisher')
    request.session['pd'] = request.POST.get('publishdate')
    request.session['pc'] = request.POST.get('price')
    try:
        Author.objects.get(Name=author1)
        return render_to_response('add_succeed.html',context_instance=RequestContext(request))        
    except Author.DoesNotExist:
        return render_to_response('add_author.html',context_instance=RequestContext(request))

def addauthor(request):
    idd = request.POST.get('author')
    name1 = request.POST.get('nam')
    age1 = request.POST.get('age')
    country1= request.POST.get('country')
    authors = Author.objects.create(AuthorID=idd,Name=name1,Age=age1,Country=country1)
    
    isbn1 = request.session['i']
    title1 = request.session['t']
    publisher1 = request.session['p']
    publishdate1 = request.session['pd']
    price1 = request.session['pc']
    
    Book.objects.create(ISBN=isbn1,Title=title1,AuthorID=authors,Publisher=publisher1,PublishDate=publishdate1,Price=price1)    
    return render_to_response('add_succeed.html',context_instance=RequestContext(request))
    
def addsucceed(request):
    return render_to_response('add_succeed.html')
    
