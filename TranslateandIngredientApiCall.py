import os
import requests
import http.client

conn = http.client.HTTPSConnection("calorieninjas.p.rapidapi.com")
from firebase import firebase
import time
from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\TULPAR\\Desktop\\BİTİRME\\braided-tracker-315323-28d9ddadc2b9.json"
firebase = firebase.FirebaseApplication('https://ne-yesek-ebf2f-default-rtdb.europe-west1.firebasedatabase.app/', None)
url = "https://api.calorieninjas.com"
engIngList = []

trIngList = []
def translate_text(target, text):
    
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language="en")

    lol = str(result["translatedText"])

    return lol


menu = []
with open('ingnamesnodp.txt') as f:
    for line in f:
        menu.append(line)
        
ingridientList = list(dict.fromkeys(menu))

        
for index, ingredient in enumerate(ingridientList):
    try:
        result = translate_text("tr",ingredient)
        engName = result
        trName = ingredient
        print(engName)
        engName =engName.replace("\n", "")
        """ headers = {
            'x-rapidapi-key': "15e853010amsh0372cddaeae2a66p1e3624jsnb06e2cef612f",
            'x-rapidapi-host': "https://api.calorieninjas.com"
            }

        ing = "/v1/nutrition?query=" + engName.replace("\n", "")
        print("/v1/nutrition?query=" + engName.replace("\n", ""))
        ing = ing.replace(" ", "%20")
        print(ing)
        conn.request("GET", ing, headers=headers)

        res = conn.getresponse()
        data = res.read()"""
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        query = engName
        response = requests.get(api_url + query, headers={'X-Api-Key': 'q6EXGco7sOH/zGTPYS9VKg==buFqBm8pwzT7WZzE'})
        
        
        data = response.text
        print(data)
        data1 = response.text
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
            
        
        res["Turkish Name"] = trName.replace("\n", "")
        res["Sugar"] = listofnumbers[0]
        res["Fiber"] = listofnumbers[1]
        res["Serving Size"] = listofnumbers[2]
        res["Sodium"] = listofnumbers[3]
        res["English Name"] = listofnumbers[4]
        res["Potassium"] = listofnumbers[5]
        res["Saturated Fat"] = listofnumbers[6]
        res["Fat"] = listofnumbers[7]
        res["Calorie"] = listofnumbers[8]
        res["Cholesterol"] = listofnumbers[9]
        res["Protein"] = listofnumbers[10]
        res["Carbohydrates"] = listofnumbers[11]
        result = firebase.post('/Ingredient/',res)
        print(result)
    except :
        if(engName != ""):
            print(ingredient)
            res["Turkish Name"] = trName.replace("\n", "")
            res["Sugar"] = "0"
            res["Fiber"] =  "0"
            res["Serving Size"] =  "0"
            res["Sodium"] =  "0"
            res["English Name"] =  engName
            res["Potassium"] =  "0"
            res["Saturated Fat"] =  "0"
            res["Fat"] =  "0"
            res["Calorie"] =  "0"
            res["Cholesterol"] =  "0"
            res["Protein"] =  "0"
            res["Carbohydrates"] =  "0"
            
            result = firebase.post('/NoNutritionIngredient/',res)
            result = firebase.post('/Ingredient/',res)
            print(result)
        else:
            print(ingredient)
            res["Turkish Name"] = trName.replace("\n", "")
            res["Sugar"] = "0"
            res["Fiber"] =  "0"
            res["Serving Size"] =  "0"
            res["Sodium"] =  "0"
            res["English Name"] = "no translation"
            res["Potassium"] =  "0"
            res["Saturated Fat"] =  "0"
            res["Fat"] =  "0"
            res["Calorie"] =  "0"
            res["Cholesterol"] =  "0"
            res["Protein"] =  "0"
            res["Carbohydrates"] =  "0"
            result = firebase.post('/NoNutritionIngredient/',res)
            result = firebase.post('/Ingredient/',res)
            print(result)
        
        