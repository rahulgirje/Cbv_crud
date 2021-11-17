from django.http import request
from django.shortcuts import redirect, render
from .models import Laptop
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class HomeView(View):
    def get(self,request):
        template_name='firstapp/Home.html'
        return render(request,template_name)



class Laptoplistview(ListView):
    model = Laptop
    template_name = 'firstapp/prod.html'

class LaptopCreateView(CreateView):
    model=Laptop
    template_name='firstapp/addprod.html'
    fields='__all__'
    success_url = '/showprod'

class LaptopUpdateView(UpdateView):
    model = Laptop
    template_name='firstapp/addprod.html'
    fields='__all__'
    success_url = '/showprod'
