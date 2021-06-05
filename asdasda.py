import requests
import http.client

conn = http.client.HTTPSConnection("calorieninjas.p.rapidapi.com")
from firebase import firebase
import time
from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication

firebase = firebase.FirebaseApplication('https://ne-yesek-ebf2f-default-rtdb.europe-west1.firebasedatabase.app/', None)
url = "https://api.calorieninjas.com"
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
            headers = {
                'X-Api-Key': "q6EXGco7sOH/zGTPYS9VKg==buFqBm8pwzT7WZzE",
            }

            
            ing = "/v1/nutrition?query=" + ingridient.replace("\n", "")
            ing = ing.replace(" ", "%20")
            conn.request("GET", ing, headers=headers)

            res = conn.getresponse()
            data = res.read()
            data1 = data.decode("utf-8")
            data1 = data1.replace('{"items": [{', "")
            data1 = data1.replace('}]}', "")
            data1 = data1.replace(' ', "",2)
            data2 = data1.split(",")
            listofnumbers = []
            res = {}
            for i in data2:
                split = i.split(":")
                split = split[1].strip()
                split = split.replace('"', "")
                listofnumbers.append(split)
                
            
            res["Turkish Name"] = trIngList[index].replace("\n", "")
            res["Sugar"] = listofnumbers[0]
            res["Fiber"] = listofnumbers[1]
            res["Serving Size"] = listofnumbers[2]
            res["Sodium"] = listofnumbers[3]
            res["English Name"] = ingridient.replace("\n", "")
            res["Potassium"] = listofnumbers[5]
            res["Saturated Fat"] = listofnumbers[6]
            res["Fat"] = listofnumbers[7]
            res["Calorie"] = listofnumbers[8]
            res["Cholesterol"] = listofnumbers[9]
            res["Protein"] = listofnumbers[10]
            res["Carbohydrates"] = listofnumbers[11]
            result = firebase.post('/Ingridient/',res)
            print(result)
            time.sleep(2)
        except :
            print(ingridient)
            res["Turkish Name"] = trIngList[index].replace("\n", "")
            res["Sugar"] = "0"
            res["Fiber"] =  "0"
            res["Serving Size"] =  "0"
            res["Sodium"] =  "0"
            res["English Name"] = ingridient.replace("\n", "")
            res["Potassium"] =  "0"
            res["Saturated Fat"] =  "0"
            res["Fat"] =  "0"
            res["Calorie"] =  "0"
            res["Cholesterol"] =  "0"
            res["Protein"] =  "0"
            res["Carbohydrates"] =  "0"
            result = firebase.post('/Ingridient/',res)
            print(result)
            time.sleep(2)
        
