from BookDB.models import Book
from BookDB.models import Author
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django import forms
from django.template import Context, RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
        return render_to_response('index.html')

def viewbook(request):
        Book_list=Book.objects.all()
        return render_to_response('viewbook.html',{'Book_list':Book_list})
@csrf_exempt
def search(req):
        ctx ={}
        #global Name
	ctx =req.POST
	ctx=ctx.get('search','')
	n=0
	if req.POST:
                Author_list=Author.objects.all()
                for Author_Name in Author_list:
                        if Author_Name.Name==ctx:
                                x=Author_Name.AuthorID
                                n=1
                if n==1:
                        Book_list=Book.objects.filter(AuthorID=x)
                        return render_to_response('search.html',{'Book_list':Book_list},context_instance=RequestContext(req))
                else:
                        erro="We can't find book the in libary"
                        return render_to_response('search.html',{'erro':erro},context_instance=RequestContext(req))
        return render_to_response('search.html',{'Book_list':Book_list},context_instance=RequestContext(req))

def delete(req):
        ctx ={}
	ctx =req.POST
	ctx=ctx.get('delete','')
	n=0
	if req.POST:
                Book_list=Book.objects.all()
                for Books in Book_list:
                        if Books.Title==ctx:
                                n=1
                if n==1:
                        Book_list=Book.objects.get(Title=ctx)
                        Book_list.delete()
                else:
                        erro="We can't find book the in libary"
                        return render_to_response('delete.html',{'erro':erro},context_instance=RequestContext(req))
        Book_list=Book.objects.all()
        return render_to_response('delete.html',{'Book_list':Book_list},context_instance=RequestContext(req))

def detail(req):
        Id = req.GET.get('id','')
        Book_list=Book.objects.get(Title=Id)
	return render_to_response('detail.html',{'Book_list':Book_list},context_instance=RequestContext(req))
