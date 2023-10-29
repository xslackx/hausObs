#!/usr/bin/env python
from requests import get, post
from dotenv import dotenv_values

class MailGun():
    def __init__(self) -> None:
        self.cfg = { **dotenv_values('.env.mailgun') }
        self.gunlink = self.cfg["LV3"]
        
    def auth(self):
        self.uri = "domains/"
        self.url = self.gunlink + self.uri + self.cfg["D"]
        self.response = get( self.url,
                                     auth=("api", self.cfg["K"]),
                                     params={ "skip": 0, "limit": 3 })
    
        return self.gun_codes(self.response.status_code)
            
        
    def send(self, message, addr):
        self.uri = "messages/"
        self.url = self.gunlink + self.cfg["D"] + "/" + self.uri
        self.response = post( self.url,
                                      auth=("api", self.cfg["K"]),
                                      data={"from": f"hausObs Mail Alert {self.cfg['L']}",
                                            "to": f"{addr}",
                                            "subject": "hausObs Alert",
                                            "text": open(message).read()}
                                      )
        return self.gun_codes(self.response.status_code)
    
    def gun_codes(self, status):
        if status == 200:
            return True
        