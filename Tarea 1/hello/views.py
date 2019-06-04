from django.shortcuts import render
from django.http import HttpResponse
import requests
import ast

from .models import Greeting


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def tarea1(request):
    # return HttpResponse('Hello from Python!')
    data = requests.get("https://swapi.co/api/films/").json()['results']
    for movie in data:
        del movie['vehicles']
        del movie['species']
    return render(request, "tarea2.html", {"data": data})

def film(request):
    if request.method=='GET':
        info = request.GET.get('info')
        info = ast.literal_eval(info)
        if not info:
            data = requests.get("https://swapi.co/api/films/").json()['results']
            return render(request, 'tarea1.html', {"data": data})
        else:
            characters = info['characters']
            characters_info = []
            for i in characters:
                character = requests.get(i).json()
                characters_info.append(character)
            planets = info['planets']
            planets_info = []
            for j in planets:
                planet = requests.get(j).json()
                planets_info.append(planet)
            starships = info['starships']
            starships_info = []
            for k in starships:
                starship = requests.get(k).json()
                starships_info.append(starship)
            return render(request, 'film.html', {"info": info, "characters": characters_info, "planets": planets_info,
                        "starships": starships_info})

def characters(request):
    if request.method=='GET':
        info = request.GET.get('info')
        info = ast.literal_eval(info)
        if not info:
            data = requests.get("https://swapi.co/api/films/").json()['results']
            return render(request, 'tarea1.html', {"data": data})
        else:
            films = info['films']
            films_info = []
            for i in films:
                film = requests.get(i).json()
                del film['vehicles']
                del film['species']
                films_info.append(film)
            starships = info['starships']
            starships_info = []
            for k in starships:
                starship = requests.get(k).json()
                starships_info.append(starship)
            planets_info = [requests.get(info['homeworld']).json()]
            return render(request, 'characters.html', {"info": info, "films": films_info, "planets": planets_info,
                        "starships": starships_info})

def planets(request):
    if request.method=='GET':
        info = request.GET.get('info')
        info = ast.literal_eval(info)
        if not info:
            data = requests.get("https://swapi.co/api/films/").json()['results']
            return render(request, 'tarea1.html', {"data": data})
        else:
            films = info['films']
            films_info = []
            for i in films:
                film = requests.get(i).json()
                del film['vehicles']
                del film['species']
                films_info.append(film)
            characters = info['residents']
            characters_info = []
            for j in characters:
                character = requests.get(j).json()
                characters_info.append(character)
            return render(request, 'planets.html', {"info": info, "films": films_info, "characters": characters_info})

def starships(request):
    if request.method=='GET':
        info = request.GET.get('info')
        info = ast.literal_eval(info)
        if not info:
            data = requests.get("https://swapi.co/api/films/").json()['results']
            return render(request, 'tarea1.html', {"data": data})
        else:
            films = info['films']
            films_info = []
            for i in films:
                film = requests.get(i).json()
                films_info.append(film)
                del film['vehicles']
                del film['species']
            pilots = info['pilots']
            pilots_info = []
            for j in pilots:
                pilot = requests.get(j).json()
                pilots_info.append(pilot)
            return render(request, 'starships.html', {"info": info, "films": films_info, "pilots": pilots_info})

def search(request):
    if request.method=="POST":
        searched = request.POST.get("input").strip()
    if not searched:
        data = requests.get("https://swapi.co/api/films/").json()['results']
        return render(request, 'tarea1.html', {"data": data})
    else:
        ## OPCION 1

        # films = []
        # for i in range(1, 8):
        #     link = "https://swapi.co/api/films/{}".format(str(i))
        #     film = requests.get(link).json()
        #     if searched.lower() in film['title'].lower():
        #         del film['vehicles']
        #         del film['species']
        #         films.append(film)


        ## OPCION 2

        films_info = requests.get("https://swapi.co/api/films/").json()['results']
        films = []
        count_f = 1
        for i in films_info:
            if searched.lower() in i['title'].lower():
                link = "https://swapi.co/api/films/{}".format(str(count_f))
                film = requests.get(link).json()
                del film['vehicles']
                del film['species']
                films.append(film)
            count_f += 1

        ## OPCION 1

        characters = []
        for j in range(1, 88):
            try:
                link = "https://swapi.co/api/people/{}".format(str(j))
                character = requests.get(link).json()
                if searched.lower() in character['name'].lower():
                    characters.append(character)
            except:
                pass

        ## OPCION 2

        # characters_info = requests.get("https://swapi.co/api/people/").json()['results']
        # characters = []
        # count_c = 1
        # for j in characters_info:
        #     try:
        #         if searched.lower() in j['name'].lower():
        #             link = "https://swapi.co/api/people/{}".format(str(count_c))
        #             character = requests.get(link).json()
        #             characters.append(character)
        #     except:
        #         pass
        #     count_c += 1


        starships = []
        for k in range(1, 38):
            try:
                link = "https://swapi.co/api/starships/{}".format(str(k))
                starship = requests.get(link).json()
                if searched.lower() in starship['name'].lower():
                    starships.append(starship)
            except:
                pass

        ## OPCION 1

        # planets = []
        # for l in range(1, 62):
        #     try:
        #         link = "https://swapi.co/api/planets/{}".format(str(l))
        #         planet = requests.get(link).json()
        #         if searched.lower() in planet['name'].lower():
        #             planets.append(starship)
        #     except:
        #         pass

        ## OPCION 2

        planets_info = requests.get("https://swapi.co/api/planets/").json()['results']
        planets = []
        count_p = 1
        for l in planets_info:
            try:
                if searched.lower() in l['name'].lower():
                    link = "https://swapi.co/api/planets/{}".format(str(count_p))
                    planet = requests.get(link).json()
                    planets.append(starship)
            except:
                pass
            count_f += 1

    return render(request, 'search.html', {"searched": searched, "films": films, "characters": characters,
                "starships": starships, "planets": planets})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
