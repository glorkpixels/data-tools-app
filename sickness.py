from firebase import firebase

from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
import json


firebase = firebase.FirebaseApplication('https://ne-yesek-ebf2f-default-rtdb.europe-west1.firebasedatabase.app/', None)



res = {}
res["Durum"] = "Diyabet"
res["Tags"] = "No Sugar"

result = firebase.post('/Preferences/',res)

res = {}
res["Durum"] = "Kolestrol"
res["Tags"] = "No Oil"

result = firebase.post('/Preferences/',res)


res = {}
res["Durum"] = "Vegan"
res["Tags"] = "No Animal Product"


result = firebase.post('/Preferences/',res)

res = {}
res["Durum"] = "Vegetarian"
res["Tags"] = "No Meat"


result = firebase.post('/Preferences/',res)
print(result)