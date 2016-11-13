from django.shortcuts import render
from .models import person
# Create your views here.
def list_persons(request):
    persons = person.objects.all()
    context = {
        'persons' : persons,
    }
    return render(request,"list.html",context)
