from django.shortcuts import render
from .models import Historia

def historia(request):
    historias = Historia.objects.all()
    return render(request, 'app_chatbot/historia.html', {'historias': historias})

