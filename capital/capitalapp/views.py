from django.shortcuts import render
from django.http import HttpResponse
import requests, json

# Create your views here.
def index(request):
    return render(request, "index.html")

def swapi(request):
        path = "https://swapi.dev/api/people/1/"
        # print(path)
        url = requests.get(path)
        print(url)
        data = json.loads(url.text)
        print(data)
        return render (request, "swapi.html", {"data": data})
        # return HttpResponse(json.dumps(data), content_type='application/json')

def films(request):
    path = request.GET["path"]
    # print(path, "")
    url = requests.get(path)
    data = json.loads(url.text)
    # print(len(bookselflink))
    return render(request, "films.html", {"data": data})
    # return HttpResponse(json.dumps(data),content_type='application/json')
    # return render(request, "films.html")

def people(request):
    path = request.GET["path"]
    # print(path, "")
    url = requests.get(path)
    data = json.loads(url.text)
    # print(len(bookselflink))
    return render(request, "swapi.html", {"data": data})
    # return HttpResponse(json.dumps(data), content_type='application/json')

def vehicles(request):
    path = request.GET["path"]
    # print(path, "")
    url = requests.get(path)
    data = json.loads(url.text)
    # print(len(bookselflink))
    return render(request, "vehicles.html", {"data": data})
    # return HttpResponse(json.dumps(data), content_type='application/json')

# def character(request):
#     path = request.GET["path"]
#     print(path, "")
#     url = requests.get(path)
#     data = json.loads(url.text)
#     # print(len(bookselflink))
#     # return render(request, "films.html", {"data": data})
#     return HttpResponse(json.dumps(data), content_type='application/json')

def starships(request):
    path = request.GET["path"]
    # print(path, "")
    url = requests.get(path)
    data = json.loads(url.text)
    # print(len(bookselflink))
    return render(request, "starships.html", {"data": data})
    # return HttpResponse(json.dumps(data), content_type='application/json')

def planets(request):
    path = request.GET["path"]
    # print(path, "")
    url = requests.get(path)
    data = json.loads(url.text)
    # print(len(bookselflink))
    return render(request, "planets.html", {"data": data})
    # return HttpResponse(json.dumps(data), content_type='application/json')

def species(request):
    path = request.GET["path"]
    # print(path, "")
    url = requests.get(path)
    data = json.loads(url.text)
    # print(len(bookselflink))
    return render(request, "species.html", {"data": data})
    # return HttpResponse(json.dumps(data), content_type='application/json')
