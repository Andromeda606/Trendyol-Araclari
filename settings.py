import random
import string

try:
    import requests
except:
    exit("requests MODÜLÜ YÜKLÜ DEĞİL! \"pip install requests\" veya \"pip3 install requests\" yazarak "
         "indirebilirsiniz.")


def get_rand_token():
    return random_str(8) + "-" + random_str(4) + "-" + "-" + random_str(4) + "-" + random_str(4) + "-" + random_str(13)


def random_str(length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(length))


def new_account(mail,passw):
    url = "https://mobile.trendyol.com/secure/json/Register"

    payload = {
        "IsConditionOfMembershipApproved": True,
        "Email": mail,
        "Gender": 1,
        "IsProtectionOfPersonalDataApproved": True,
        "Password": passw
    }

    headers = {
        "Host": "mobile.trendyol.com",
        "X-Storefront-Id": "1",
        "X-Application-Id": "5",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) Trendyol/5.8.3.513",
        "Build": "5.8.3.513",
        "Platform": "Android",
        "Gender": "F",
        "Searchsegment": "31",
        "Osversion": "7.1.1",
        "Deviceid": get_rand_token(),
        "Pid": get_rand_token(),
        "Sid": get_rand_token(),
        "X-Features": "REBATE_ENABLED",
        "Accept-Language": "tr-TR",
        "Uniqueid": random_str(16),
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "150",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code == 429:
        exit("HATA! IP niz geçici süreliğine kısıtlandı, ip değiştirmek için modemi kapat aç veya uçak modunu aç kapat yapabilirsin.")
    else:
        f = open("openedmails.txt", "a")
        f.write(mail + ":" + passw + "\n")
        f.close()
        return response.text
