from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse
from . import pool
# Create your views here.
def index(request):
    data = True
    result = None
    globalSummary = None
    while(data):
        try:
            result = requests.get("https://api.covid19api.com/summary")
            globalSummary = result.json()['Global']
            data = False
        except:
            data = True

    return render(request, 'index.html',{'globalSummary': globalSummary})



def CountriesData(request):
    data = True
    result = None
    countries = None
    while(data):
        try:
            result = requests.get("https://api.covid19api.com/summary")
            json = result.json()
            countries = json['Countries']
            data = False
        except:
            data = True

    return render(request, 'countries_data.html', {'countries': countries})


def CountriesDataJSON(request):
    data = True
    result = None
    countries = None
    country = None
    while(data):
        try:
            search = request.POST.get('search', False)
            #print(search)
            result = requests.get("https://api.covid19api.com/summary")
            json = result.json()
            result = json["Countries"]
            for j in result:
               if j['Country'] == search.capitalize():
                    country = j
                    break
            data = False
            #print(country)
            return render(request, 'search.html', {'country': country})
        except Exception as e:
            print(e)
            data=True
            return render(request, 'search.html', {'msg': 'server error'})

def countryDatabase(request):
   try:
     db,cmd=pool.ConnectionPooling()
     result = requests.get("https://api.covid19api.com/summary")
     json = result.json()
     result = json["Countries"]
     for j in result:
        country = j['Country']
        totalconfirmed = j['TotalConfirmed']
        totaldeaths = j['TotalDeaths']
        totalrecovered = j['TotalRecovered']
        q="insert into countrydata(country,totalconfirmed,totaldeath,totalrecovered) values('{0}','{1}','{2}','{3}')".format(country,totalconfirmed,totaldeaths,totalrecovered)

        print(q)
        cmd.execute(q)
     db.commit()
     db.close()
     return render(request, "countries_data.html")
   except Exception as e:
     print(e)
     return render(request, "countries_data.html")

