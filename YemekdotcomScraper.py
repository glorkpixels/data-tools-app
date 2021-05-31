# -*- coding: utf-8 -*-
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
webpagelist = []
ingamounts = []
ingnames = []

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


    breadcrumb = soup.find("div", {"class" : "breadcrumbContainer"}).find("div" ,{"class" : "breadcrumbsCont"}).text
    print(breadcrumb)

    image = soup.find("div", {"class" : "MainImage printHidden"}).find("img")
    print(image)
    
    xd1 = str(image)
    lol1 = xd1.split("src=")
    imageline = lol1[1]
    vlparsed1 = imageline.split(" ",1)
    vl1 = vlparsed1[0]
    imagelink = vl1.replace('"','')


    title = soup.find("h1", {"class" : "titleSecondPiece"}).text


    prep = ""
    prepinfo = soup.find("div", {"class" : "topInfo"})
    for xd in   prepinfo.find_all("div", {"class" : "prepTime"}):
        prep += xd.find("p").text + ";"


    ingridients = ""
    ingridientslist= ""


    for tarifler in soup.find_all("div", {"class" : "recipeIngredient"}):
        itemqty = ""
        itemname = ""
        for spans in tarifler.find_all("span", {"class" : "recipeItemQty"}):
        # print(str(spans.text.encode('utf-8').decode("cp1252")))
            itemqty =str(spans.text)
            
        for spans in tarifler.find_all("span", {"class" : "recipeItemName"}):
        # print(str(spans.text.encode('utf-8').decode("cp1252")))
            itemname =str(spans.text)

        ingridients +=  "● " +(itemqty +" "+itemname+"\n")
        ingridientslist += (itemname +";")
        ingamounts.append(itemqty)
        ingnames.append(itemname)
        
  

    recipe = ""
    point =1
    for tarifler in soup.find("ol", {"class" : "recipeList"}).find_all("li"):
        itemqty = ""
        for spans in tarifler.find_all("p"):
            itemqty =str(spans.text)
        item = itemqty 
        recipe += str(point) + ".) " + item + '\n'
        point +=1
    #print(recipe)
    #print(ingridientslist)

    
    jsonx = soup.find_all('script', type='application/ld+json')
    workcount =0
    print(len(jsonx))
    print(jsonx[0])
    x = str(jsonx[0])
    x = x.split('<script data-react-helmet="true" type="application/ld+json">')
    x = x[1]
    x = x.split('</script>')
    x = x[0]
    print(x)
    
 
    strx = "{" + x+ "}"
  
        
    print(strx)
        
    print("lol")
    lol = json.loads(x) #a dictionary!

    maincategory = lol["recipeCategory"]
    Keywords = lol["keywords"]
    Cuisine = lol["recipeCuisine"]
    ShortDescription = lol["description"]


    data =  { 
            
            'Name': title,
            'RecipeDetails': recipe,
            'Ingridients': ingridients,
            'IngridientNames': ingridientslist,
            'PrepDetails' : prep,
            'CategoryBread': breadcrumb,
            'MainCategory' : maincategory,
            'Keywords' : Keywords,
            'ShortDescription' : ShortDescription,
            'Cuisine' : Cuisine,
            'Image':imagelink
            } 

    print(title)
    #text_file = open("RecipeLinks-From-Yemekcom.txt", "w", encoding='utf-8')
   # text_file.write(str(data))
    #text_file.close()
    #result = firebase.post('/Recipe/'+maincategory+"/",data)
    result = firebase.post('/Recipe/',data)
    print(result)

"""with open('ingquantity.txt', 'a', "utf-8") as filehandle:
    filehandle.writelines("%s\n" % amounth for amounth in ingamounts)"""
    
f = open('ingquantity.txt', 'a')
for i in ingamounts:
      if(i != ""):
            f.write(i +"\n")

f.close()


ingridientList = list(dict.fromkeys(ingnames))

f = open('ingnames.txt', 'a')
for i in ingridientList:
    if(i != ""):
        f.write(i +"\n")
    
f.close()
  
    
"""with open('ingnames.txt', 'a', "utf-8") as filehandle:
    filehandle.writelines("%s\n" % name for name in ingnames)"""

