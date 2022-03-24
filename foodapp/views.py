from django.shortcuts import render
from .forms import FoodForm
from django.http.response import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Food
from django.urls import reverse_lazy
# Create your views here.
# belows functionalities using FBV
'''
def index(req):
    return render(req,'foodapp/index.html')


def addfood(req):
    
    rn HttpResponse('<h2> Food is Added....</h1>')
    else:
        foodform = FoodForm()
    data = {'foodform':foodform}
    return render(req,'foodapp/foodform.html',data)
'''
#Now we Convert the FBV functionalities in CBV

class FoodCreateView(CreateView):
    model = Food
    form_class=FoodForm
    template_name = "foodapp/foodform.html"
    success_url = reverse_lazy('foodmenu')

# above view will form object for Food Automatically with form name

class FoodListView(ListView):
    model=Food
    template_name='foodapp/foodmenu.html'
    context_object_name='flist'
'''
    default values as follow
        tmplate_name = 'appname/modelname_list.html' 
        context_object_name = object_list

'''    

class FoodUpdateView(UpdateView):
    model = Food
    template_name = "foodapp/foodform.html"
    form_class=FoodForm
    success_url=reverse_lazy('foodmenu')

class FoodDeleteView(DeleteView):
    model=Food
    success_url=reverse_lazy('foodmenu')

class FoodDetailView(DetailView):
    model=Food
    template_name='foodapp/foodmenu.html'
