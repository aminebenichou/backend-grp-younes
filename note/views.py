from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
# Create your views here.
def home(request):
    notes = Note.objects.all()
    context = {
        'notes':notes
    }
    return render(request, "index.html", context)


def createNote(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        note = Note.objects.all()
        note.create(title=title, content=content)
    return render(request, 'createNote.html')

def deleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect(home)