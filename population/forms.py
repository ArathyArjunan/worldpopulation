from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from population.models import Worldpopulation 


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class SearchForm(forms.Form):
    query = forms.CharField()

class PopulationCreateForm(forms.ModelForm):
    class Meta:
        model=Worldpopulation
        fields="__all__"
        widgets={
        
            "place":forms.NumberInput(attrs={"class":"form-control"}),
            "pop1980":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2000":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2010":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2022":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2023":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2050":forms.NumberInput(attrs={"class":"form-control"}),
            "country":forms.TextInput(attrs={"class":"form-control"}),
            "area":forms.NumberInput(attrs={"class":"form-control"}),
            "landAreaKm":forms.NumberInput(attrs={"class":"form-control"}),
            "cca2":forms.TextInput(attrs={"class":"form-control"}),
            "cca3":forms.TextInput(attrs={"class":"form-control"}),
            "netChange":forms.TextInput(attrs={"class":"form-control"}),
            "growthRate":forms.TextInput(attrs={"class":"form-control"}),
            "worldPercentage":forms.TextInput(attrs={"class":"form-control"}),
            "density":forms.TextInput(attrs={"class":"form-control"}),
            "densityMi":forms.TextInput(attrs={"class":"form-control"}),
            "rank":forms.NumberInput(attrs={"class":"form-control"})


            
            
            

            



            

   
    }
        


class PopulationChangeForm(forms.ModelForm):
    class Meta:
        model=Worldpopulation
        fields="__all__"
        widgets={
        
            "place":forms.NumberInput(attrs={"class":"form-control"}),
            "pop1980":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2000":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2010":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2022":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2023":forms.NumberInput(attrs={"class":"form-control"}),
            "pop2050":forms.NumberInput(attrs={"class":"form-control"}),
            "country":forms.TextInput(attrs={"class":"form-control"}),
            "area":forms.NumberInput(attrs={"class":"form-control"}),
            "landAreaKm":forms.NumberInput(attrs={"class":"form-control"}),
            "cca2":forms.TextInput(attrs={"class":"form-control"}),
            "cca3":forms.TextInput(attrs={"class":"form-control"}),
            "netChange":forms.TextInput(attrs={"class":"form-control"}),
            "growthRate":forms.TextInput(attrs={"class":"form-control"}),
            "worldPercentage":forms.TextInput(attrs={"class":"form-control"}),
            "density":forms.TextInput(attrs={"class":"form-control"}),
            "densityMi":forms.TextInput(attrs={"class":"form-control"}),
            "rank":forms.NumberInput(attrs={"class":"form-control"})


            
            
            

            



            

   
    }
        
   