import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\TULPAR\\Desktop\\BİTİRME\\braided-tracker-315323-28d9ddadc2b9.json"

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

        
for name in ingridientList:
    try:
        result = translate_text("tr",name)

        #print(name + "Turkce")
        #print(result.text + " English")
        #print(result.pronunciation)
        engName = result
        trName = name
        #parsedName= engName.replace(" ", "+")
        #print(parsedName )
        f = open('ingnamesenglish.txt', 'a')
        if "("  in engName: 
            string = engName.replace("(")
            lol = string.split("(")
            print(engName)
            engName= lol[0]
            print(engName)
            f.write(engName +"\n")
        else:
            f.write(engName +"\n")
            
            
        f.close()
    except :
        pass
    
def translate_text(target, text):

    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language="en")

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

