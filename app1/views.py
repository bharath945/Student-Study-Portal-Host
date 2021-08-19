from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from app1 import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from app1 import forms
from app1 import models
from youtubesearchpython import VideosSearch
import requests
import wikipedia
# Create your views here.
def home(request):
    return HttpResponseRedirect("accounts/login")
@login_required
def dashbord(request):
    return render(request,"app1/Dashbord.html")
@login_required
def notes(request):
    form=forms.Notes()
    dict1={}
    dict1["meassage"]=""
    if request.method=="POST":
        form1=forms.Notes(request.POST)
        if form1.is_valid():
            form2=models.Notes(user=request.user,title=request.POST["title"],description=request.POST["description"])
            form2.save()
            dict1["meassage"]="Data Added Successfully"
    data=models.Notes.objects.filter(user=request.user)
    dict1["form"]=form
    dict1["data"]=data
    return render(request,"app1/notes.html",context=dict1)
@login_required
def homework(request):
    form=forms.Homework()
    if request.method=="POST":
        form1=forms.Homework(request.POST)
        if form1.is_valid():
            model2=models.Homework(user=request.user,subject=request.POST["subject"],title=request.POST["title"],description=request.POST["description"],due=request.POST["due"])
            model2.save()
    data=models.Homework.objects.filter(user=request.user)
    return render(request,"app1/homework.html",{"data":data,"form":form})
@login_required
def youtube(request):
    form=forms.search()
    dict1={}
    dict1["form"]=form
    if request.method=="POST":
        data=request.POST["data"]
        video=VideosSearch(data,limit=10)
        result_list=[]
        for i in video.result()["result"]:
            result_dict={
                'input':data,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'publushed':i['publishedTime'],
                }
            desc=""
            if i["descriptionSnippet"]:
                for j in i["descriptionSnippet"]:
                    desc+=j['text']
            result_dict["description"]=desc
            result_list.append(result_dict)
            dict1["results"]=result_list
    return render(request,"app1/youtube.html",dict1)
@login_required
def todo(request):
    dict1={}
    if request.method=="POST":
        form2=forms.Todo(request.POST)
        if form2.is_valid():
            mod=models.Todo(user=request.user,data=request.POST["data"],status=False)
            mod.save()
            dict1["message"]="Data added to Todo successfully"
    form1=forms.Todo()
    dict1["form"]=form1 
    dict1["data"]=models.Todo.objects.filter(user=request.user)
    return render(request,"app1/todo.html",dict1)
@login_required
def books(request):
    form=forms.search()
    dict1={}
    dict1["form"]=form
    if request.method=="POST":
        data=request.POST["data"]
        url="https://www.googleapis.com/books/v1/volumes?q="+data
        r=requests.get(url)
        answer=r.json()
        result_list=[]
        for i in range(10):
            result_dict={
                'title':answer['items'][i]["volumeInfo"]["title"],
                'subtitle':answer['items'][i]["volumeInfo"].get("subtitle"),
                'description':answer['items'][i]["volumeInfo"].get("description"),
                'count':answer['items'][i]["volumeInfo"].get("pagecount"),
                'categories':answer['items'][i]["volumeInfo"].get("categories"),
                'rating':answer['items'][i]["volumeInfo"].get("pagerating"),
                'thumbnail':answer['items'][i]["volumeInfo"].get('imagelinks'),
                'preview':answer['items'][i]["volumeInfo"].get("previewLink")
                }
            result_list.append(result_dict)
            dict1["results"]=result_list
    return render(request,"app1/books.html",dict1)
@login_required
def dictionary(request):
    form=forms.search()
    dict1={}
    dict1["form"]=form
    if request.method=="POST":
        data=request.POST["data"]
        url="https://ap1.dictionaryapi.dev/api/v2/entries/en_US/"+data
        r=requests.get(url)
        ans=r.json()
        try:
            dict1["phonetics"]=ans[0]['phonetics'][0]['text']
            dict1["audio"]=ans[0]['phonetics'][0]['audio']
            dict1["definition"]=ans[0]['meanings'][0]['definitions'][0]['definition']
            dict1["example"]=ans[0]['meanings'][0]['definitions'][0]['example']
            dict1["synonyms"]=ans[0]['phonetics'][0]['definitions'][0]['synonyms']
            dict1["input"]=data
        except:
            dict1["input"]=""
    return render(request,"app1/dictionary.html",dict1)
@login_required
def wiki(request):
    form1=forms.search()
    dict1={}
    dict1["form"]=form1
    if request.method=="POST":
        try:
            data=request.POST["data"]
            form=forms.search(request.POST)
            search=wikipedia.page(data)
            dict1["title"]=search.title
            dict1["link"]=search.url
            dict1["details"]=search.summary
        except:
            dict1["valid"]="Data Not Found"
    return render(request,"app1/wiki.html",dict1)
@login_required
def conversion(request):
    return render(request,"app1/conversion.html")

def register(request):
    form=forms.Register()
    if request.method=="POST":
        form=forms.Register(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login")
    return render(request,"app1/register.html",{"form":form})
def delNotes(request,id):
    model=models.Notes.objects.get(id=id)
    model.delete()
    return redirect("/notes")
def notesshow(request,id):
    data=models.Notes.objects.get(id=id)
    return render(request,"app1/notesshow.html",{"data":data})
def homedel(request,id):
    data=models.Homework.objects.get(id=id)
    data.delete()
    return redirect("/homework")
def deltodo(request,id):
    models.Todo.objects.get(id=id).delete()
    return redirect("/todo")
def todoup(request,id):
    data=models.Todo.objects.get(id=id)
    if data.status==True:
        data.status=False 
    else:
        data.status=True
    data.save()
    return redirect("/todo")
def profile(request):
    return render(request,"app1/profile.html")