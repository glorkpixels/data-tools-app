import googletrans
from googletrans import Translator

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

webSiteUrl = "https://www.nutritionvalue.org"
translator = Translator()

ingridientList = []
with open('ingnames.txt') as f:
    for line in f:
        ingridientList.append(line)
        
for name in ingridientList:
    result = translator.translate(name)
    """
    print(result.src)
    print(result.dest)
    print(result.origin)
    """
    #print(name + "Turkce")
    #print(result.text + " English")
    #print(result.pronunciation)
    engName = result.text
    trName = name
    parsedName= engName.replace(" ", "+")
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


'''
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(webSiteUrl)
wait = WebDriverWait(driver, 10)	

# usr
el = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
el.send_keys("username@gmail.com")
el.send_keys(Keys.ENTER)
'''