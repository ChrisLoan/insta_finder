from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests

# Create your models here.

def index(request):
    id = ""
    i = 0
    if request.method == "POST":
        username = request.POST.get("username")
        url = "https://instagram-scraper-2022.p.rapidapi.com/ig/user_id/"
        querystring = {"user":username}
        headers = {
            "X-RapidAPI-Key": "3970f2bd64mshf7fccab22b4493bp1fbadfjsn8c44d90460cc",
            "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
        }
        responses = requests.request("GET", url, headers=headers, params=querystring)
        res = responses.json()
        for a in  res.values():
            id = a
            break
        url = "https://instagram-scraper-2022.p.rapidapi.com/ig/info/"

        querystring = {"id_user":id}

        headers = {
            "X-RapidAPI-Key": "3970f2bd64mshf7fccab22b4493bp1fbadfjsn8c44d90460cc",
            "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        cont_follow = response.json()["user"]["follower_count"]
        cont_follower = response.json()["user"]["following_count"]
        media_count = response.json()["user"]["media_count"]
        return render(request,'photo/resultat.html',context={"follower":cont_follow,"following":cont_follower,"post_count":media_count})
    return render(request,'photo/index.html')
