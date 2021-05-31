import requests
from firebase import firebase

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
       
        jeez = ingridient + " " + "100 grams"
        jeez.strip("\n")
        querystring = {"ingr": jeez }
        print(querystring)

        headers = {
            'x-rapidapi-key': "15e853010amsh0372cddaeae2a66p1e3624jsnb06e2cef612f",
            'x-rapidapi-host': "edamam-edamam-nutrition-analysis.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)