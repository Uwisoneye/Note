from django.shortcuts import render
from .models import Note

def home(request):
    all_notes = Note.objects.all()

    context = {"notes": all_notes}
    return render(request, "home.html", context=context)