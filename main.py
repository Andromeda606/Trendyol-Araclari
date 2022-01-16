import time

import settings

def send_save():
    print("Kaydetme göndermek için hesapları seçin")

    print("1- Elle hesap gir")
    print("2- openedmails.txt üzerinden çek")

    while True:
        try:
            status = input("")
            if status == "1":  # int e çevirebilirdim ama gerek yok.
                print(
                    "Hesapları mail:şifre formatında giriniz (örn abc@gmail.com:bubirsifre) sonra iki kez entere "
                    "basınız")
                mails = '\n'.join(iter(input, '')).strip().split("\n")
                _send_save(mails)

            elif status == "2":
                _send_save(open("openedmails.txt", encoding="utf-8").read().strip().split("\n"))

            else:
                print("Lütfen tekrar gir")
                continue


        except Exception as e:
            print("Bir hata oluştu, tekrar dene lütfen.")
            print("Hata: " + str(e))
            send_save()


def _send_save(mails):
    print("Koleksiyon listesini giriniz, koleksiyon listesi ty.gl ile başlayan veya linkte \"k-\" geçen koleksiyonlar olmalı. Her koleksiyonda entere basın ve koleksiyon kalmayınca 2 kere entere basın.")
    print("Örnek: https://ty.gl/bubirkoleksiyonlinki\nhttps://www.trendyol.com/koleksiyonlar/BUDABIRLINK-k-ID\n\ngibi.")

    collections = '\n'.join(iter(input, '')).strip().split("\n")
    for collection in collections:
        for x in mails:
            element = x.split(":")
            while True:
                status = settings.loginMobile(element[0], element[1])
                if status == "IPCHANGE":
                    print("IP Bloklaması yaşandı, lütfen ip değiştirin. 2 saniye sonra tekrar denenecek.")
                    time.sleep(2)
                    continue
                break
            print(settings.go_save(settings.get_collection_id(collection), status["accessToken"]))


    print("Bizi tercih ettiğiniz için teşekkürler, bütün işlem tamamlandı!")
    start()


def openaccount():
    print("Hesap Açma Türünü Seçin")

    print("1- Elle mail gir")
    print("2- Random Mailler ile")
    while True:
        status = input("")
        if status == "1":  # int e çevirebilirdim ama gerek yok.
            print("Mailleri giriniz (örn abc@gmail.com) sonra iki kez entere basınız")

            mails = '\n'.join(iter(input, '')).strip().split("\n")

            passw = input("Açılacak hesapların şifresini giriniz: ")

            for x in mails:
                while True:
                    status = settings.new_account(x, passw)
                    if status == "IPCHANGE":
                        print("IP Bloklaması yaşandı, lütfen ip değiştirin. 2 saniye sonra tekrar denenecek.")
                        time.sleep(2)
                    else:
                        print(x + " hesabı Açıldı!")
                        break
        
            print("Bizi tercih ettiğiniz için teşekkürler, bütün hesaplar açıldı!")
            start()

        elif status == "2":

            passw = input("Açılacak hesapların şifresini giriniz: ")

            for x in range(10):
                while True:
                    mail = settings.random_str(6) + "@gmail.com"
                    status = settings.new_account(mail, passw)
                    if status == "IPCHANGE":
                        print("IP Bloklaması yaşandı, lütfen ip değiştirin. 2 saniye sonra tekrar denenecek.")
                        time.sleep(2)
                    else:
                        print(mail + " hesabı Açıldı!")
                        break
            print("Bizi tercih ettiğiniz için teşekkürler, bütün hesaplar açıldı!")
            start()

        else:
            print("Lütfen tekrar gir")
            continue


def getcoupon():
    print("hesapları mail:şifre formatında giriniz (örn abc@gmail.com:bubirsifre) sonra iki kez entere basınız")
    list = '\n'.join(iter(input, '')).strip().split("\n")
    f = open("kuponlistesi.txt", "a", encoding='utf8')
    f.write("\n----------------------------- YENİ KUPON LİSTESİ ----------------------\n")

    for x in list:
        account = x.split(":")
        while True:
            status = settings.loginMobile(account[0], account[1])
            if status == "IPCHANGE":
                print("IP Bloklaması yaşandı, lütfen ip değiştirin. 2 saniye sonra tekrar denenecek.")
                time.sleep(2)
                continue
            break
        couponlist = settings.get_cupons(status["accessToken"])["coupons"]
        for x in range(len(couponlist)):
            element = couponlist[x]
            data = "\nHesabın maili: " + account[0] + "\nKupon türü: " + element[
                "couponDiscountAmountText"] + "\nKupon Başlığı: " + element["couponTitle"] + "\nKupon açıklaması: " + \
                   element["couponDescription"] + "\nKupon bitiş tarihi: " + element["couponExpirationDate"] + "\n\n\n"
            f.write(data)

    f.close()
    print("İşlem tamamlandı! kuponlar \"kuponlistesi.txt\" dosyasına aktarıldı")
    start()


def start():
    print("----------------------")
    print("Androsoft Trendyol Aracı")
    print("R10 Androsoft")
    print("Instagram: @ramazan_3_")
    print("----------------------")
    print()
    print("Yapılacak işlemi seçin")
    print("1- Hesap Açma")
    print("2- Kupon Sorgulama")
    print("3- Koleksiyon Kaydedici")

    while True:
        status = input()
        if status == "1":
            openaccount()
        elif status == "2":
            getcoupon()
        elif status == "3":
            send_save()
