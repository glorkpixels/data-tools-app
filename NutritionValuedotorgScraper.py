from os import link
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
from urllib.request import Request, urlopen
from firebase import firebase
import time

from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
import json
import unicodedata
import googletrans
from googletrans import Translator


webSiteUrlSearch = "https://www.nutritionvalue.org/search.php?food_query="
webSiteUrl = "https://www.nutritionvalue.org"
firebase = firebase.FirebaseApplication('https://ne-yesek-ebf2f-default-rtdb.europe-west1.firebasedatabase.app/', None)
def hasNumbers(inputString):
    return any( 48 <= ord(char) <= 57 for char in inputString)

engIngList = []

trIngList = []
with open('ingnames.txt') as f:
    for line in f:
        trIngList.append(line)

with open('ingnamesenglish.txt') as f:
    for line in f:
        engIngList.append(line)
        


for index, ingridient in enumerate(engIngList):
    try:
        
    
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
        table = soup.find("table", {"class" : "center zero"}).find_all("td" , {"class" : "left"})
        table2 = soup.find("table", {"class" : "center zero"}).find_all("tr")
        
        
        
        detailList = []
        for i in table2:
            xd = ""
            nonBreakSpace = u'\xa0'
            col1 = i.find("td" , {"class" : "left"})
            
            col2 = i.find("td" , {"class" : "right"})
            
            if col1 != None:
                if col2 != None:
                    if (col1.text== "Amount Per Serving"):
                        xd = "Calorie" + "*****" + col2.text
                    else:
                        xd = col1.text + "*****" + col2.text
                    
            lol = xd.replace('\xa0', ' ')
            lol.strip()
            f = open('deneme.txt', 'a')
            detailList.append(lol)
            if(lol != ""):
                f.write(lol +"\n")
            #print(lol)
            f.close()
            
        images = soup.find_all("img")
        imagesx= []
        for x in range(len(images)):
            if images[x]["src"] != "/images/question2.png":
                imagesx.append(images[x]["src"] )
                
                
        if len(imagesx) ==4:
            lol = imagesx[0]
            imagesx[0]= webSiteUrl + "/"+ lol
        
        data = ""
        datalist = []
        datalistpair = []
        while("" in detailList) :
            detailList.remove("")
        for x in detailList:
            i= x.split("*****")
            #print(i)
            
            if i[0] == "":
                i.pop(0)
                i.pop(1)
                i.pop(2)
                i.pop(3)
                

            left = i[0]
            right = i[1]
            #print(left)
            #print(right)
            if left == "Serving Size" or left == "Calorie":
                if left == "Calorie":
                    data +='"' +left +'"'+ ": " + right
                    
                    datalist.append(left) 
                    datalistpair.append(right)
                else :
                    data +='"' +left +'"'+ ": " + right + " , "
                    datalist.append(left) 
                    datalistpair.append(right)
                
            else:
                SplitLeft = left.split(" ")
                pointer = 0
                for i in range(len(SplitLeft)):
                    if hasNumbers(SplitLeft[i]):
                        #print(SplitLeft[i])
                        pointer = i
                        
                Temp = ""
            # print(pointer)
                #print("here")
                for i in range(pointer):
                    Temp += SplitLeft[i] + " "
                
                datalist.append(Temp.strip())
                datalistpair.append(SplitLeft[pointer])
                if right == "":
                    datalist.append("Daily " + Temp.strip() )
                    datalistpair.append("NaN")
                else:
                    datalist.append("Daily " + Temp.strip() )
                    datalistpair.append(right)
    
        res = {}
        for key in datalist:
            for value in datalistpair:
                
                res[key.replace('"',"")] = value
                datalistpair.remove(value)
                break  
        res["Turkish Name"] = TrName
        res["English Name"] = name[0]
        if len(imagesx) ==4:
            res["Image Header"] = imagesx[0]
            res["Image data1"] = imagesx[1]
            res["Image data2"] = imagesx[2]
        
        if len(imagesx) ==3:
            res["Image data1"] = imagesx[0]
            res["Image data2"] = imagesx[1]
        
        with open("sample.json", "w") as outfile: 
            json.dump(res, outfile)
        
        result = firebase.post('/Ingridients/',res)
        print(result)
        time.sleep(2)
    except Exception as e:
        print(e)
        pass
    
    
