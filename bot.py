from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import winsound
from datetime import datetime
import getpass

buyingStatus = True
username = getpass.getuser()

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data")


productLink = input("Lütfen ürün linkini giriniz : ")
productAmount = input("Lütfen satın almak istediğiniz ürün miktarını giriniiz :  ")
accountPass = input("Lütfen şifrenizi giriniz(İsteğe bağlı) : ")
driver = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe", options=options)

driver.get(productLink)
while(buyingStatus):
    try:
        baslangic = datetime.now()
        beGreedy = Select(driver.find_element_by_id('quantity'))
        beGreedy.select_by_value(productAmount)
        addCart = driver.find_element_by_id("add-to-cart-button").submit()
        completeTheShopping = driver.find_element_by_id("hlb-ptc-btn-native").click()

        if driver.title == "Amazon Giriş Yap":
            driver.find_element_by_id("ap_password").send_keys(accountPass)
            driver.find_element_by_id("signInSubmit").click()


        buyNow = driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input").click()
        bitis = datetime.now()
        print(bitis - baslangic)
        freq = 500
        dur = 2000
        winsound.Beep(freq, dur)
        buyingStatus = False

            

    except NoSuchElementException:
        print("ITEM DOESN'T EXIST")
        driver.refresh()
        
        

