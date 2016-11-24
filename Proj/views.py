from django.shortcuts import render, redirect
from .models import person
from django.views.generic import DetailView, View
from .forms import insertForm
from django.contrib.auth.decorators import login_required

def list_persons(request):
    search_query = request.GET.get('search_box','')
    none = search_query
    if not search_query:
        context = {

        }
    else:
        persons = person.objects.filter(id_number=search_query).values('name', 'id_number', 'address', 'age','date_added')
        if not persons:
            context = {
                "person" : False,
                'none_id' : none,
            }
        else:
            context = {
                'person' : persons,
            }
    return render(request,"list.html",context)

@login_required
def Person2add(request):
    if request.method == 'POST':
        form = insertForm(request.POST)
        if form.is_valid():
            newPerson = person()
            newPerson.name = form.cleaned_data['name']
            newPerson.id_number = form.cleaned_data['id_number']
            newPerson.age = form.cleaned_data['age']
            newPerson.address = form.cleaned_data['address']
            newPerson.save()
            return redirect('home')
    else:
        form = insertForm()
        content = {
            "form" : form,
        }
        return render(request,"insert.html",content)

@login_required
def listAll(request):
    persons = person.objects.values('name', 'id_number', 'address', 'age','date_added')
    context = {
        "person" : persons,
    }
    return render(request,"listall.html",context)

def home(request):
    return render(request, "home.html")
