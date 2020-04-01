# Python Nike Bot
# Arthur Xu
# March 23rd, 2020
# Nike Canada Bot

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys
from multiprocessing import Process
from threading import Thread

#Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--no-sandbox') 
driver = webdriver.Chrome(options=chrome_options)

#taskNum = input()
taskNum = 1

def runTasks(taskNum):

    driver.get("Enter link here")

    time.sleep(5)
    driver.refresh()
    startTime = time.time()
    print("Start task #"+ str(taskNum))

    #Getting the size
    driver.implicitly_wait(10)
    split1 = time.time()
    print("Page Opened after ", split1-startTime)
    driver.execute_script("window.scrollTo(0, 400)") 
    sizeButton=driver.find_elements_by_xpath("//button[contains(string(), 'US SIZE HERE')]")[0]
    split2 = time.time()
    print("Size Found after ", split2-split1)
    #time.sleep(3)
    sizeButton.click()

    addToBag=driver.find_elements_by_xpath("//button[contains(string(), 'ADD TO BAG')]")[0]
    addToBag.click()

    goToCheckout = driver.find_elements_by_xpath("//button[contains(string(), 'Checkout')]")[0]
    goToCheckout.click()

    split3 = time.time()
    print("Carted after ", split3-split2)

    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.NAME, "firstname")))
    finally:
        print("")
    #Filling in info
    first_name = driver.find_element_by_name("firstname")
    first_name.click()
    first_name.send_keys("First Name")

    last_name = driver.find_element_by_id("Shipping_LastName")
    last_name.click()
    last_name.send_keys("Last Name")

    PostalCode = driver.find_element_by_id("Shipping_PostCode")
    PostalCode.click()
    PostalCode.send_keys("Postal Code")

    try:
        beans = WebDriverWait(driver, 15).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spiner-holder")))
    finally:
        print("")

    address = driver.find_element_by_id("Shipping_Address1")
    address.click()
    address.send_keys("Address")

    town = driver.find_element_by_id("Shipping_Address3")
    town.click()
    town.send_keys("City")

    pn = driver.find_element_by_id("Shipping_phonenumber")
    pn.click()
    pn.send_keys("Phone Number")

    email = driver.find_element_by_id("shipping_Email")
    email.click()
    email.send_keys("Email")

    driver.find_element_by_class_name("checkbox-checkmark").click()
    split4 = time.time()
    print("Filled in address after ", split4-split3)

    #time.sleep(1)
    # Going to billing
    continueToBilling = driver.find_element_by_id("shippingSubmit")
    continueToBilling.click()

    contToPayment=driver.find_elements_by_xpath("//button[contains(string(), 'Continue to Payment')]")[0]
    contToPayment.click()

    # Filling in billing
    checkoutForm = driver.find_element_by_id("paymentIFrame")
    formLink = checkoutForm.get_attribute("ng-src")

    driver.get(formLink)

    creditName = driver.find_element_by_name('CreditCardHolder')
    creditName.click()
    creditName.send_keys("Credit Card Name")

    CC = driver.find_element_by_name('KKnr')
    CC.click()
    CC.send_keys("Credit Card Number")

    CC = driver.find_element_by_name('KKnr')
    CC.click()
    CC.send_keys("Credit Card Number")

    CCMonth = Select(driver.find_element_by_name('KKMonth'))
    CCMonth.select_by_visible_text('Month') #01, 02, ..., 11, 12
    CCMonth.select_by_value('Month')

    CCYear = Select(driver.find_element_by_name('KKYear'))
    CCYear.select_by_visible_text('Year')
    CCYear.select_by_value('Year')

    CCSC = driver.find_element_by_name('CCCVC')
    CCSC.click()
    CCSC.send_keys("CCV")

    split5 = time.time()
    print("Filled in billing after ", split5-split4)

    submit = driver.find_element_by_id('BtnPurchase')
    submit.click()

    split6 = time.time()
    print("COPPED after ", split6-split5)
    print("Total time: ", split6-startTime)

runTasks(taskNum)