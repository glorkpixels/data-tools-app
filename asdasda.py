import requests
import http.client

conn = http.client.HTTPSConnection("calorieninjas.p.rapidapi.com")
from firebase import firebase
import time
from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication

firebase = firebase.FirebaseApplication('https://ne-yesek-ebf2f-default-rtdb.europe-west1.firebasedatabase.app/', None)
url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"
engIngList = []

trIngList = []
with open('ingnames.txt') as f:
    for line in f:
        trIngList.append(line)

with open('ingnamesenglish.txt') as f:
    for line in f:
        engIngList.append(line)
        
        
for index, ingridient in enumerate(engIngList):       
        
        headers = {
            'x-rapidapi-key': "15e853010amsh0372cddaeae2a66p1e3624jsnb06e2cef612f",
            'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
            }

        
        ing = "/v1/nutrition?query=" + ingridient.replace("\n", "")
        ing = ing.replace(" ", "%20")
        conn.request("GET", ing, headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
