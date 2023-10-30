#!/usr/bin/env python
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import dotenv_values

class EditorOnline():
    def __init__(self) -> None:
        self.cfg = { **dotenv_values(".env.bootstrapmail") }
        self.website = self.cfg["URL"]
        self.driver = webdriver.Chrome()
        self.selectors = [
            "/html/body/form/div/div[1]/div[3]/a[1]",
            "/html/body/div/div[1]/div/div/form/label[1]/input",
            "/html/body/div/div[1]/div/div/form/label[2]/input",
            "/html/body/div/div[1]/div/div/form/input[2]",
        ]
        
    def auth(self):
        self.driver.get(self.website)
        sleep(3)
        self.driver.find_element(By.XPATH, self.selectors[0]).click()
        sleep(3)
        self.driver.find_element(By.XPATH, self.selectors[1]).send_keys(self.cfg["U"])
        self.driver.find_element(By.XPATH, self.selectors[2]).send_keys(self.cfg["P"])
        self.driver.find_element(By.XPATH, self.selectors[3]).click()
        
    def out(self):
        pass
    
    def model(self):
        pass