from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.core.cache import cache


# Create your views here.

BANXICO_TOKEN = "e8af177d1ad56394543b528c1e4791a75dabf29d6307dfff67fa452379fd7d9b"

def home(request):
    return render(request, 'core/home.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            
            return redirect('home')
    
    return render(request, 'registration/register.html', data)

def exit(request):
    logout(request)
    return redirect("home")

def get_exchange():
    cache_key='tipo_cambio_banxico'
    type_exchange_data = cache.get(cache_key)
    
    if isinstance(type_exchange_data, dict) and "tipo_cambio" in type_exchange_data and "fecha" in type_exchange_data:
        return type_exchange_data["tipo_cambio"], type_exchange_data["fecha"]
    
    
    url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno"
    headers = {"Bmx-Token": BANXICO_TOKEN}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if "bmx" in data and "series" in data["bmx"] and data["bmx"]["series"]:
            serie = data["bmx"]["series"][0]
            if "datos" in serie and serie["datos"]:
                exchange_rate = float(serie["datos"][0]["dato"])
                date = serie["datos"][0]["fecha"]
                
                type_exchange_data = {"tipo_cambio": exchange_rate, "fecha": date}

                cache.set(cache_key, type_exchange_data, timeout=60 * 15)
                
                return exchange_rate, date
    
    return None, None

@login_required
def exchange(request):
    exchange_rate, date = get_exchange()
    
    return render(request, "core/exchange.html", {
        "date": date,
        "exchange_rate": exchange_rate,
    })

            
            