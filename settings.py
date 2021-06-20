import random
import string

import os
import time

try:
    import requests
except:
    exit("requests MODÜLÜ YÜKLÜ DEĞİL! \"pip install requests\" veya \"pip3 install requests\" yazarak "
         "indirebilirsiniz.")

def adb(code):
    os.system("adb " + code)


def change_airplane(data):
    if data is True:
        adb("shell settings put global airplane_mode_on 1")
        adb("shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")
    else:
        adb("shell settings put global airplane_mode_on 0")
        adb("shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")


def airplane_change():
    change_airplane(True)
    time.sleep(4)
    change_airplane(False)
    time.sleep(4)

def get_rand_token():
    return random_str(8) + "-" + random_str(4) + "-" + "-" + random_str(4) + "-" + random_str(4) + "-" + random_str(13)


def random_str(length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(length))


def new_account(mail, passw):
    url = "https://loginapp.trendyol.com/register/user"

    payload = {
        "guestToken": "",
        "preferences": [
            {
                "id": 0,
                "isAccept": True
            }
        ],
        "regulation": {
            "isConditionOfMembershipApproved": True,
            "isProtectionOfPersonalDataApproved": True
        },
        "user": {
            "email": mail,
            "gender": 2,
            "password": passw,
            "storeFrontId": "1",
            "userType": "MEMBER"
        }
    }

    headers = {
        "Host": "loginapp.trendyol.com",
        "X-Storefront-Id": "1",
        "X-Application-Id": "5",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) Trendyol/5.10.3.521",
        'Build': "5.10.3.521",
        "Platform": "Android",
        "Gender": "F",
        "Searchsegment": "31",
        "Deviceid": get_rand_token(),
        "Pid": get_rand_token(),
        "Sid": get_rand_token(),
        "X-Features": "REBATE_ENABLED",
        "Accept-Language": "tr-TR",
        "Uniqueid": random_str(16),
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    if response.status_code == 429:
        print("HATA IP DEĞİŞTİRİN")
    else:
        if "accessToken" in response.text:
            f = open("openedmails.txt", "a")
            f.write(mail + ":" + passw + "\n")
            f.close()
        return (response.text)


def favorite_item(id,bearer):
    url = "https://api.trendyol.com/webaccountgw/api/favorites/?storefrontId=1&culture=tr-TR"

    payload = {
        "itemNumbers": [],
        "brandId": 682,
        "brandName": "Slazenger",
        "categoryId": 429,
        "categoryName": "Yürüyüş Ayakkabısı",
        "contentId": id,
        "contentName": "Erkek Siyah Yürüyüş Ayakkabısı",
        "favoritedPrice": 118.7
    }

    headers = {
        "Authorization": "Bearer " + bearer,
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "api.trendyol.com",
        "Origin": "https://www.trendyol.com",
        "Referer": "https://www.trendyol.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
    print(response.status_code)


def login(email, passw):
    url = "https://auth.trendyol.com/login"

    payload = {
        "guestToken": "",
        "password": passw,
        "email": email
    }

    headers = {
        "Build": "5.8.3.513",
        "Platform": "Android",
        "Gender": "M",
        "Searchsegment": "31",
        "Osversion": "7.1.1",
        "Deviceid": get_rand_token(),
        "Pid": get_rand_token(),
        "Sid": get_rand_token(),
        "application-id": "1",
        "storefront-id": "1",
        "culture": "tr-TR",
        "X-Features": "REBATE_ENABLED",
        "Accept-Language": "tr-TR",
        "Uniqueid": random_str(16),
        "X-Storefront-Id": "1",
        "X-Application-Id": "5",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; SAMSUNG A5000 Build/NMF26X) Trendyol/5.8.3.513",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "X-Newrelic-Id": "VQQAUV9aGwEFXVNVBgk=",
        "Connection": "close"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()


def loginMobile(email, passw):
    url = "https://loginapp.trendyol.com/auth/token"

    payload = {
        "guestToken": "",
        "password": passw,
        "username": email
    }

    headers = {
        "Build": "5.8.3.513",
        "Platform": "Android",
        "Gender": "M",
        "Searchsegment": "31",
        "Osversion": "7.1.1",
        "Deviceid": get_rand_token(),
        "Pid": get_rand_token(),
        "Sid": get_rand_token(),
        "application-id": "1",
        "storefront-id": "1",
        "culture": "tr-TR",
        "X-Features": "REBATE_ENABLED",
        "Accept-Language": "tr-TR",
        "Uniqueid": random_str(16),
        "X-Storefront-Id": "1",
        "X-Application-Id": "5",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; SAMSUNG A5000 Build/NMF26X) Trendyol/5.8.3.513",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "X-Newrelic-Id": "VQQAUV9aGwEFXVNVBgk=",
        "Connection": "close"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.json()


def get_cupons(bearer):
    url = "https://zeusapi.trendyol.com/mobile-zeus-zeuscheckout-service/coupon"

    querystring = {"page": "1", "couponContext": "COUPON"}

    payload = ""
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) Trendyol/5.8.3.513",
        "X-Storefront-Id": "1",
        "X-Application-Id": "5",
        "Build": "5.8.3.513",
        "Platform": "Android",
        "Gender": "M",
        "Searchsegment": "31",
        "Osversion": "7.1.1",
        "Deviceid": get_rand_token(),
        "Pid": get_rand_token(),
        "Sid": get_rand_token(),
        "X-Features": "REBATE_ENABLED",
        "Accept-Language": "tr-TR",
        "Uniqueid": random_str(16),
        "Authorization": "bearer " + bearer,
        "Accept-Encoding": "gzip, deflate",
        "X-Newrelic-Id": "VQQAUV9aGwEFXVNVBgk=",
        "Connection": "close"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return response.json()

