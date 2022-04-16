import time

import requests as req
import re


class Mail:
    email = ""

    def __init__(self):
        self.email = req.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]

    def get_inbox(self):
        params = self.email.split("@")
        return req.get("https://www.1secmail.com/api/v1/?action=getMessages&login=" + params[0] + "&domain=" + params[1]).json()

    def get_verification_code(self):
        while True:
            time.sleep(0.3)
            inbox = self.get_inbox()
            if len(inbox) == 1:
                regex = r"KOD: (.*?)$"
                matches = re.finditer(regex, inbox[0]["subject"], re.MULTILINE)
                for matchNum, match in enumerate(matches, start=1):
                    return match.group(1)

