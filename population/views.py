from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from population.forms import RegistrationForm,LoginForm,PopulationCreateForm,SearchForm,PopulationChangeForm
from django.views.generic import View,ListView,DetailView,UpdateView,TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from population.models import Worldpopulation
from django.utils.decorators import method_decorator
from django.http import HttpResponse



def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session, please login to your account")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration completed successfully")
            return redirect("signin")
        else:
            messages.error(request,"Registration failed")
            return render(request,"signup.html",{"form":form})    


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials !")
                return render(request,"signin.html",{"form":form})  
            

class IndexView(ListView):
   template_name="index.html"
   context_object_name="population"
   model=Worldpopulation
    
   def get_queryset(self):
        qs=Worldpopulation.objects.all()
        return qs
class search_view(View):
        def search(self,request,*args, **kwargs):
            form=SearchForm(request.POST)
            if form.is_valid():
                uname=form.cleaned_data.get("search")
                
                if Worldpopulation.country==uname:
                    result=Worldpopulation.objects.get(country=uname) 
                    return render(request,"search.html",{"result":result})
                else:
                    messages.error(request,"invalid credentials !")
                    return render(request,"signin.html",{"result":result})



class PopulationCreateView(View):
    def get(self,request,*args,**kwargs):
        form=PopulationCreateForm()
        return render(request,"population_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=PopulationCreateForm(request.POST)
        if form.is_valid():
            # form.save()
            Worldpopulation.objects.create(**form.cleaned_data)
            messages.success(request,"Added success")
            return redirect("index")
        else:
            messages.error(request,"insertion failed")
            return render(request,"population_add.html",{"form":form})


@method_decorator(signin_required,name="dispatch")              
class PopulationDetailView(DetailView):
    template_name="population_detail.html"
    context_object_name="pop"
    model=Worldpopulation
    
@method_decorator(signin_required,name="dispatch")               
class PopulationUpdateView(UpdateView):
    template_name="population_edit.html"
    success_url=reverse_lazy("index")
    form_class=PopulationChangeForm
    model=Worldpopulation
    
@signin_required
def remove_population(request,*args,**kwargs):
   id=kwargs.get("pk")
   Worldpopulation.objects.get(id=id).delete()
   return redirect("index")


def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
    
