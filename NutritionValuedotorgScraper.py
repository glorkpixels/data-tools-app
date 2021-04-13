from os import link
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
from urllib.request import Request, urlopen
from firebase import firebase

from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
import json




webSiteUrlSearch = "https://www.nutritionvalue.org/search.php?food_query="
webSiteUrl = "https://www.nutritionvalue.org"
firebase = firebase.FirebaseApplication('https://ne-yesek-ebf2f-default-rtdb.europe-west1.firebasedatabase.app/', None)


engIngList = []

trIngList = []
with open('ingnames.txt') as f:
    for line in f:
        trIngList.append(line)

with open('ingnamesenglish.txt') as f:
    for line in f:
        engIngList.append(line)
        


for index, ingridient in enumerate(engIngList):
    
    search = ingridient.replace(" ", "+")
    
    webpage = webSiteUrlSearch + search
    #print(webpage)
    req = Request(webpage, headers={'User-Agent': 'Mozilla/5.0'},)
    webpagex = urlopen(req).read()
  

    #html_page = urllib.request.urlopen(webpagelist[0])
    soup = BeautifulSoup(webpagex, 'html.parser')
    #print(soup.original_encoding)
    link = soup.find("table", {"class" : "full_width results zero"}).find("td", {"class" : "left"})
    
    link = soup.find("table", {"class" : "full_width results zero"}).find("td", {"class" : "left"}).find("a", href=True)["href"]
    
    name = soup.find("table", {"class" : "full_width results zero"}).find("td", {"class" : "left"}).find("a")["title"]

    
    print(link)
    name = str(name).split(",")
    print(name[0])
    
    
    EngName = name
    TrName = trIngList[index]
    LinkToGo = webSiteUrl + link
    print(LinkToGo)
    req2 = Request(LinkToGo, headers={'User-Agent': 'Mozilla/5.0'},)
    webpagedetail = urlopen(req2).read()

    #html_page = urllib.request.urlopen(webpagelist[0])
    soup = BeautifulSoup(webpagedetail, 'html.parser')
    print(soup)
    
    
    
        