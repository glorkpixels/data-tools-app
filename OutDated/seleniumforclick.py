from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')


driver = webdriver.Chrome(ChromeDriverManager().install())