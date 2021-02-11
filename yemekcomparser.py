# -*- coding: utf-8 -*-
from os import link
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
from urllib.request import Request, urlopen
from firebase import firebase
import json
from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication

webpagelist = []

firebase = firebase.FirebaseApplication('https://ne-yesek-ebf2f-default-rtdb.europe-west1.firebasedatabase.app/', None)


with open('RecipeLinks-From-Yemekcom.txt') as f:
    for line in f:
        webpagelist.append(line)
        

print(webpagelist)


for webpage in webpagelist:
    req = Request(webpage, headers={'User-Agent': 'Mozilla/5.0'},)
    webpage = urlopen(req).read()

    #html_page = urllib.request.urlopen(webpagelist[0])
    soup = BeautifulSoup(webpage, from_encoding="utf-8")
    print(soup.original_encoding)


    image = soup.find("div", {"class" : "MainImage printHidden"}).find("img")
    xd1 = str(image)
    lol1 = xd1.split("src=")
    imageline = lol1[1]
    vlparsed1 = imageline.split(" ",1)
    vl1 = vlparsed1[0]
    imagelink = vl1.replace('"','')
    #print(imagelink)



    title = soup.find("h1", {"class" : "titleSecondPiece"}).text
    #print(title)

    ingridients = []
    ingridientslist= []
    for tarifler in soup.find_all("div", {"class" : "recipeIngredient"}):
        itemqty = ""
        itemname = ""
        for spans in tarifler.find_all("span", {"class" : "recipeItemQty"}):
        # print(str(spans.text.encode('utf-8').decode("cp1252")))
            itemqty =str(spans.text)
            
        for spans in tarifler.find_all("span", {"class" : "recipeItemName"}):
        # print(str(spans.text.encode('utf-8').decode("cp1252")))
            itemname =str(spans.text)

        ingridients.append(itemqty)
        ingridients.append(itemname)
        ingridientslist.append(itemname)
        #print(str(tarifler.text.encode('utf-8').decode("cp1252")))


    #print(ingridients)


    recipe = []
    for tarifler in soup.find("ol", {"class" : "recipeList"}).find_all("li"):
        itemqty = ""
    # print(tarifler.text.encode('utf-8').decode("cp1252"))
        for spans in tarifler.find_all("p"):
        # print(str(spans.text.encode('utf-8').decode("cp1252")))
            
            itemqty =str(spans.text)
            
    
        item = itemqty 
        recipe.append(item)
        #print(str(tarifler.text.encode('utf-8').decode("cp1252")))

    #print(recipe)



    #print(ingridientslist)

    


    steps = { "recipe" : recipe
    }

    translationTable = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")




    recipestr = str(recipe)
    choices = {"İ":"I", "ş" : "s", "Ş":"s" ,"ğ": "g" , "Ğ":"g"}

    #print(recipestr)
    ingstr = str(ingridients)
    ingstr = ingstr.translate(translationTable)
    inglist = str(ingridientslist)
    inglist = inglist.translate(translationTable)





    data =  { 'Name': title,
            'Recipe': recipe,
            'Ingridients': ingridients,
            'IngridientNames': ingridientslist,
            'image':imagelink
            } 

    print(title)
    #text_file = open("RecipeLinks-From-Yemekcom.txt", "w", encoding='utf-8')
   # text_file.write(str(data))
    #text_file.close()
    result = firebase.post('/Recipe/',data)
    print(result)













"""
with open('data.json', 'w',encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False,indent=4,)

for link in soup.find("div", {"class" : "parts ingredients"}):
    
    anan = str(link.text.encode('utf-8').decode("cp1252"))
    link.find("")
    print(anan) 
    """