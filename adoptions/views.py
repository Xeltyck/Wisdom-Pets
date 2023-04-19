from django.shortcuts import render
from django.http import HttpResponse #Needs to be imported if used (duhh). It's ued to provide an HTTP response (duhh x2). Not handy if using a lot of HTML. 
#Useful just for a quick test. Better use the render function. it has the task of rendering html onto the templates.
# template files will be needeed in order to work.

from django.http import Http404 #Needs to be imported if 404 implementation is needed.

# Create your views here.
from .models import Pet # We have to import Pet in order to use the model Queries that were stablished. 

def home(request):
    pets = Pet.objects.all()
    return render(request,'home.html',{"pets":pets}) # Last argument is the data we want available inside of the template. Dictionary, key-value pair.Key is created and value is the query variable created before.

def pet_detail(request,pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)# If a request of a non existing id is made, Try Except with Error 404 is needed.
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request,'pet_detail.html',{'pet':pet}) #Both html files need to be created in a templates folder insside the app folder (adoptions)
        
   