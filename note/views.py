from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
# Create your views here.
def home(request):
    message = "Your balance is : 50000 DZD"
    context = {
        'message':message
    }
    return render(request, "index.html", context)


def createNote(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        note = Note.objects.all()
        note.create(title=title, content=content)
    return render(request, 'createNote.html')