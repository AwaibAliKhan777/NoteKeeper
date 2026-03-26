from django.shortcuts import render, redirect
from .models import Note

def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.create(title=title , content=content)
        return redirect('/')
    
    notes = Note.objects.all()
    return render(request, 'home.html' , {'notes' : notes})

def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('/')

def update_note(request,id):
    note = Note.objects.get(id=id)

    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('/')
    
    return render(request, 'update.html', {'note':note})