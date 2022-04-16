import random
import string

import os
import time
from urllib.parse import urlparse
from temp_mail import Mail

try:
    import requests
except:
    os.system("python -m pip3 install requests")
    exit("requests MODÜLÜ YÜKLÜ DEĞİL! \"pip install requests\" veya \"pip3 install requests\" yazarak "
         "indirebilirsiniz. (Otomatik yüklemeyi denedi, önce tekrar çalıştırmayı deneyin)")


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


def new_account(mail, passw, otp=None):
    email = None
    url = "https://auth.trendyol.com/v2/signup"
    if mail is None:
        email = Mail()
        mail = email.email

    payload = {
        "email": mail,
        "marketingEmailsAuthorized": False,
        "password": passw,
        "genderId": -1,
        "conditionOfMembershipApproved": True,
        "protectionOfPersonalDataApproved": True,

    }
    if otp is not None:
        payload["otpCode"] = otp

    headers = {
        "X-Storefront-Id": "1",
        "X-Application-Id": "5",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) Trendyol/5.10.3.521",
        'Build': "6.13.3.616",
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
        "Culture": "tr-TR",
        "Storefront-Id": "1",
        "Application-Id": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 429:
        return "IPCHANGE"
    else:
        if otp is None:
            print(mail + " Maili ile hesap açılıyor.")
            if email is not None:
                print("Onay kodu aranıyor, biraz uzun sürebilir.")
                res = new_account(mail, passw, email.get_verification_code())
            else:
                res = new_account(mail, passw, input("Onay Kodunu Giriniz"))
        else:
            return response.text
        if "accessToken" in res:
            f = open("openedmails.txt", "a")
            f.write(mail + ":" + passw + "\n")
            f.close()
        return (res)

def login(email, passw):
    url = "https://loginapp.trendyol.com/auth/token"

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

    if response.status_code == 429:
        return "ERROR429"
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


def go_save(id, bearer):
    url = "https://browsingpublic-mdc.trendyol.com/mobile-zeus-zeussocial-service/zeus/mycollections/" + id + "/follow"

    headers = {
        'Host': "browsingpublic-mdc.trendyol.com",
        'Authorization': "bearer " + bearer,
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) Trendyol/5.10.3.521",
        'Build': "5.10.3.521",
        'Platform': "Android",
        'Gender': "M",
        'Searchsegment': "31",
        'Osversion': "7.1.1",
        "Deviceid": get_rand_token(),
        "Pid": get_rand_token(),
        "Sid": get_rand_token(),
        "X-Features": "REBATE_ENABLED",
        "Accept-Language": "tr-TR",
        "Uniqueid": random_str(16),
        'X-Storefront-Id': "1",
        'X-Application-Id': "5",
        'Content-Length': "0",
        'Accept-Encoding': "gzip, deflate",
        'X-Newrelic-Id': "VQQAUV9aGwEFXVNVBgk=",
        'Connection': "close"
    }

    response = requests.request("POST", url, headers=headers)
    print(response.text)
    print(response.status_code)


def query_to_dict(query: str) -> dict:
    returned = {}
    for x in query.split("&"):
        element = x.split("=")
        returned[element[0]] = element[1]
    return returned


def get_collection_id(link) -> str:
    # ID yi fark etmemi sağlayan "do6an" adlı Github kullanıcısına teşekkürler.

    if "ty.gl" in link:
        url = urlparse(requests.get(link).url)
        querys = query_to_dict(url.query)
        if "link_collectionID" in querys:
            return querys["link_collectionID"]
        elif "utm_campaign" in querys:
            return querys["utm_campaign"]
        else:
            path = url.path
            return path[path.index("k-") + 2:]
    elif "k-" in link:
        path = urlparse(link).path
        return path[path.index("k-") + 2:]
