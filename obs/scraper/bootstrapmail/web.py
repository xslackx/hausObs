#!/usr/bin/env python
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
        
    def auth(self):
        pass