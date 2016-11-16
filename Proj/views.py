from django.shortcuts import render
from .models import person
from django.views.generic import DetailView, View
# Create your views here.
def list_persons(request):
    new_persons = {}
    if request.method == 'GET':
        search_query = request.GET.get('search_box',None)
        if search_query is not None:
            persons = person.objects.filter(id_number=search_query).values('name', 'id_number', 'address', 'age')
            persons = persons[0]
            print(persons)
            # for k,v in persons.iteritems():
            #     k = k.replace("_"," ")
            #
            #     new_persons[k]=[v]
            # print(new_persons)
            persons['id number'] = persons.pop('id_number')
            context = {
                'person' : persons
                }
            print(context)
            return render(request,"list.html",context)
        else:
            return render(request,"list.html")

class PersonDetails(DetailView):
    model = person
    template_name = "person.html"

def update(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        id_number = request.GET.get('id_number')
        age = request.GET.get('age')
        address = request.GET.get('address')
        context = {
            'resp' : True
        }
    return render(request,"update.html",context)
