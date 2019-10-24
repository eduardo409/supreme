
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time

class Purchase:
    links = {
            "shirts":"https://www.supremenewyork.com/shop/all/shirts",
            "t-shirts": "https://www.supremenewyork.com/shop/all/t-shirts",
            "jackets":"https://www.supremenewyork.com/shop/all/jackets",
            "tops_sweaters":"https://www.supremenewyork.com/shop/all/tops_sweaters",
            "hats":"https://www.supremenewyork.com/shop/all/hats",
            "accessory":"https://www.supremenewyork.com/shop/all/accessories",
            "pants":"https://www.supremenewyork.com/shop/all/pants",
            "sweatshirts": "https://www.supremenewyork.com/shop/all/sweatshirts",
            "bags": "https://www.supremenewyork.com/shop/all/bags",
            "skate": "https://www.supremenewyork.com/shop/all/skate"
        }

    def __init__(self, item, client, frequency):
        print('\n\nNew Purchase initiated\n\n', client, item)
        self.url = self.links[item.item_type]
        self.clientItem = item
        self.client = client 
        self.frequency = frequency
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images":2}
        chromeOptions.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome('../chromedriver')
        # self.driver.get(url) 

    def start(self):
        start = time.time()
        item = self.waitForItem().click()
        self.addToCart()
        self.checkout()
        end = time.time()
        print("time: ",end - start, "seconds")
        
    def checkout(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'order_billing_name')))
        self.fillForm()

                              
    def addToCart(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'commit'))).click()
        time.sleep(.5)
        self.driver.get('https://www.supremenewyork.com/checkout')

    def waitForItem(self):
        items = self.getItems() 
        found = self.compareItems(items, self.clientItem)
        while not found:
            time.sleep(self.frequency)
            items = self.getItems()
            found = self.compareItems(items, self.clientItem)
        return found 

    def compareItems(self, listOfItems, clientItem):
        # todo check for size and color 
        for item in listOfItems:
            if clientItem.name.lower() in item.text.lower():
                return item
        return None
    # returns a list of items found on page
    def getItems(self):
        self.driver.get(self.url) 
        element_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'inner-article'))
        items = WebDriverWait(self.driver, 5).until(element_present)
        # items = self.driver.find_elements_by_class_name('inner-article')
        return items

    def printItems(self,items):
        for item in items:
            print('item:', item.text.lower().replace('\n', ' ').replace('\r', ''))


    def __del__(self):
        print('destroying object')
        # self.driver.close()

    def fillForm(self):
        # client info
        fullname = '"{} {}"'.format(self.client.fName, self.client.lName)
        name = 'document.getElementById("order_billing_name").setAttribute("value",{} );'.format(fullname)
        email = 'document.getElementById("order_email").setAttribute("value","{}");'.format(self.client.email)
        phone = 'document.getElementById("order_tel").setAttribute("value", "{}");'.format(self.client.phone)
        address = 'document.getElementById("bo").setAttribute("value", "{}");'.format(self.client.credit.address)
        zipCode = 'document.getElementById("order_billing_zip").setAttribute("value", "{}");'.format(self.client.credit.zipCode)
        city = 'document.getElementById("order_billing_city").setAttribute("value", "{}");'.format(self.client.credit.city)
        country = 'document.getElementById("order_billing_country").setAttribute("value", "USA");'
        self.driver.find_element_by_name("order[billing_state]").send_keys(self.client.credit.state)
        self.driver.execute_script(name + email + phone + address + zipCode + city + country)
        # client payment 
        cardNumber = 'document.getElementById("cnb").setAttribute("value", "{}");'.format(self.client.credit.cardNumber)
        self.driver.execute_script(cardNumber)
        # i change the input format here because changing the following elements with the java scrip method t(above code) wouldnt
        # explicitly show the changes on the site. could lead to some user confusion when using bot.
        self.driver.find_element_by_name("credit_card[year]").send_keys(self.client.credit.year)
        self.driver.find_element_by_name("credit_card[month]").send_keys(self.client.credit.month)
        self.driver.find_element_by_name("credit_card[vvv]").send_keys(self.client.credit.cv)

        self.driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "iCheck-helper", " " ))]')[1].click()
        # process payment click
        self.driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "button", " " ))]').click()

