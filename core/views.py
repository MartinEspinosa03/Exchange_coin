from .models import ExchangeRate
from .models import ExchangeRateDOF
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.core.cache import cache
from datetime import datetime, date
from bs4 import BeautifulSoup



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
    today = datetime.today().date()

    exchange_entry = ExchangeRate.objects.filter(date=today).first()
    if exchange_entry:
        return exchange_entry.rate, exchange_entry.date.strftime("%Y-%m-%d")

    url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno"
    headers = {"Bmx-Token": BANXICO_TOKEN}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if "bmx" in data and "series" in data["bmx"] and data["bmx"]["series"]:
            serie = data["bmx"]["series"][0]
            if "datos" in serie and serie["datos"]:
                exchange_rate = float(serie["datos"][0]["dato"])
                date_str = serie["datos"][0]["fecha"]  
                
                date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()
                
                exchange_entry, created = ExchangeRate.objects.get_or_create(
                    date=date_obj, 
                    defaults={"rate": exchange_rate}
                    )

                return exchange_entry.rate, exchange_entry.date.strftime("%Y-%m-%d")
    
    return None, None

            
def get_currency_exchange_dof():
    url = "https://www.dof.gob.mx/indicadores.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, verify=False, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        tables = soup.find_all("table")

        if len(tables) >= 15:  
            table = tables[14]

            paragraphs = table.find_all("p")
            for p in paragraphs:
                span = p.find("span", class_="tituloBloque4")
                if span:
                    indicator = span.get_text(strip=True).upper()
                    value = p.get_text(strip=True).replace(indicator, "").strip()

                    if "DOLAR" in indicator:
                        currency_exchange = float(value.replace(',', ''))
                        today = datetime.today().date().strftime("%Y-%m-%d")
                        return currency_exchange, today
        
        print("No se encontró el valor del dólar.")
    else:
        print(f"Error al acceder a la página: {response.status_code}")
        
    return None, None
                    
    
def save_currency_exchange_dof():
    currency_exchange, dateDof = get_currency_exchange_dof()
    
    if currency_exchange is not None and dateDof is not None:
        ExchangeRateDOF.objects.update_or_create(
            date=dateDof,
            defaults={'currency_exchange': currency_exchange}
        )
        return currency_exchange, dateDof
    else:
        return None, None
     
@login_required
def exchange(request):
    exchange_rate, date_obj = get_exchange()
    last_exchange, last_date = save_currency_exchange_dof()
    
    return JsonResponse({
        "date": date_obj,
        "exchange_BANXICO": exchange_rate,
        'exchange_DOF': float(last_exchange) if last_exchange is not None else None
    })     