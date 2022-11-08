#imports
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import os
import wget

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument("start-maximized")
prefs = {"credentials_enable_service": False,
     "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#code is here
try:
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Hp\OneDrive\Desktop\chromedriver_win32\chromedriver",options=options
    )
except:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # This will install the updated chromedriver automatically.

driver.get('https://www.facebook.com/')

username=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='email']")))
password=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='pass']")))

username.clear()
#Here you have to enter your email or phone
username.send_keys("--------- email or phone ----------")
password.clear()
#Here you have to enter your password
password.send_keys("--------Enter Password----------")

log_in=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()

images=[]
#https://www.facebook.com/zamanali181818/photos_by
for i in ['photos_by','photos_of']:
    #Here you just have to put the link of your facebook link that is opened in the browser
    driver.get(Yourid_link_when_you_open_your_photos  +i+"/")
    time.sleep(5)
    for j in range(1,2):
        driver.execute_script("window.scroll(0,document.body.scrollHeight);")
        time.sleep(5)
        anchors = driver.find_elements(By.TAG_NAME, 'a')
        anchors=[a.get_attribute('href') for a in anchors]
        anchors=[a for a in anchors if str(a).startswith('https://www.facebook.com/photo')]
        for a in anchors:
            driver.get(a)
            time.sleep(5)
            img=driver.find_elements(By.TAG_NAME,"img")
            images.append(img[1].get_attribute("src"))




#Saving the images into Your Computer
path=os.getcwd()
path=os.path.join(path, 'ScrapedPhotos')
os.mkdir(path)

counter=0
for image in images:
    save_as=os.path.join(path,str(counter) + '.jpg')
    wget.download(image,save_as)
    counter=counter+1


