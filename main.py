import settings


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
                print(settings.new_account(x, passw))

            print("Bizi tercih ettiğiniz için teşekkürler, bütün hesaplar açıldı!")

        elif status == "2":

            passw = input("Açılacak hesapların şifresini giriniz: ")

            for x in range(10):
                print(settings.new_account(settings.random_str(15) + "@gmail.com", passw))

            print("Bizi tercih ettiğiniz için teşekkürler, bütün hesaplar açıldı!")

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
        couponlist = settings.get_cupons(settings.loginMobile(account[0], account[1])["accessToken"])["coupons"]
        for x in range(len(couponlist)):
            element = couponlist[x]
            data = "\nHesabın maili: " + account[0] + "\nKupon türü: " + element[
                "couponDiscountAmountText"] + "\nKupon Başlığı: " + element["couponTitle"] + "\nKupon açıklaması: " + \
                   element["couponDescription"] + "\nKupon bitiş tarihi: " + element["couponExpirationDate"] + "\n\n\n"
            f.write(data)

    f.close()
    print("İşlem tamamlandı! kuponlar \"kuponlistesi.txt\" dosyasına aktarıldı")


print("----------------------")
print("Androsoft Trendyol Aracı")
print("R10 Androsoft")
print("Instagram: @ramazan_3_")
print("----------------------")
print()
print("Yapılacak işlemi seçin")
print("1- Hesap Açma")
print("2- Kupon Sorgulama")

while True:
    status = input()
    if status == "1":
        openaccount()
    elif status == "2":
        getcoupon()
