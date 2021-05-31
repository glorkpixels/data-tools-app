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

    """    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
        print(lol)
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))"""
    
    lol = str(result["translatedText"])

    return lol

    

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
'''

menu = []
with open('ingnames.txt') as f:
    for line in f:
        menu.append(line)
        
ingridientList = list(dict.fromkeys(menu))

        
for name in ingridientList:
    try:
        result = translate_text("tr",name)
        """
        print(result.src)
        print(result.dest)
        print(result.origin)
        """
        #print(name + "Turkce")
        #print(result.text + " English")
        #print(result.pronunciation)
        engName = result
        trName = name
        #parsedName= engName.replace(" ", "+")
        #print(parsedName )
        f = open('ingnamesenglish.txt', 'a')
        if(engName != ""):
            if engName == "its":	
                    f.write("water" +"\n")
            elif engName == "a":
                f.write("flour" +"\n")
            elif engName == "mince" and trName == "kıyma":
                f.write("ground beef" +"\n")
            else:
                if engName != "":
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

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language="en")

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


'''
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(webSiteUrl)
wait = WebDriverWait(driver, 10)	

# usr
el = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
el.send_keys("username@gmail.com")
el.send_keys(Keys.ENTER)
'''