from selenium import webdriver
from selenium.webdriver.chrome.service import DEFAULT_EXECUTABLE_PATH, Service
from selenium.webdriver.chrome.webdriver import DEFAULT_KEEP_ALIVE, DEFAULT_PORT, DEFAULT_SERVICE_LOG_PATH
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

DRIVER_PATH = r"C:\Users\hi\Documents\SeleTest\src\chromedriver.exe"
LINK = "https://page.auctions.yahoo.co.jp/jp/auction/k1091491414"



class MyDriver(webdriver.Chrome):

    def __init__(self):
        executable_path = DRIVER_PATH
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super().__init__(executable_path, chrome_options=chrome_options)

    def access(self, link):
        self.get(link)
    
    def remove_ads(self):
        ads_box_s  = self.find_elements(By.CLASS_NAME, "prMdl__bgWrap")
        if len(ads_box_s) > 0:
            # x_ads_box = self.find_element(By.CLASS_NAME, "prMdl__close")
            # x_ads_box.click()
            time.sleep(0)
            print("Skip ads")
            actions = ActionChains(self)
            actions.move_by_offset(1,1).click().perform()
            time.sleep(0)
    def get_name(self):
        item_name = ""
        #get item name
        item_names = self.find_elements(By.CLASS_NAME, 'ProductTitle__text')
        if len(item_names) == 1:
            item_name = item_names[0].text
            print("item_name: " + item_name)
        elif len(item_names) >1:
            print("Too many item name element")
        else:
            print ("Can't find item name")
        return item_name
    def get_id(self):
        id = 0
        url = self.current_url
        ids = re.findall("[0-9]{7,}")
        if len(ids) == 1:
            id = ids[0].text
            print("item_name: " + id)
        elif len(ids) >1:
            print("Too many id element")
        else:
            print ("Can't find id element")
        return id
    def get_category_tree(self):
        category_tree = []
        category_tree_elems = self.find_elements(By.CLASS_NAME, 'Section__categoryList')
        if len(category_tree_elems)==1:
            category_tree_elem = category_tree_elems[0]
            categories = category_tree_elem.find_elements(By.XPATH, "./*")
            for i in categories:
                print("Category: " + i.text)
                category_tree.append(i.text)
        return category_tree
    def get_data(self):
        data = {}
        data["name"] = self.get_data()
        data["id"] = self.get_id()
        data["category"]
        

mydrive = MyDriver()
mydrive.access(LINK)
mydrive.remove_ads()
mydrive.get_name()
mydrive.get_category_tree()

