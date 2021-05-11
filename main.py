import settings
import random
import string

print("----------------------")
print("Androsoft Trendyol Hesap Açıcı")
print("R10 Androsoft")
print("Instagram: @ramazan_3_")
print("----------------------")
print()
print("Hesap Açma Türünü Seçin")
print("1- Mail listesi (Max 10 mail, fazlasında trendyol ip nizi kısıtlıyor.)")
print("2- Random Mailler ile")

def random_str(length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(length))


while True:
    status = input("")
    if status == "1": #int e çevirebilirdim ama gerek yok.
        passw = input("Açılacak hesapların şifresini giriniz: ")

        mails = open("openedmails.txt", "r", encoding="utf8").read().split("\n")

        for x in mails:
            print(settings.new_account(x, passw))

        print("Bizi tercih ettiğiniz için teşekkürler, bütün hesaplar açıldı!")

    elif status == "2":

        passw = input("Açılacak hesapların şifresini giriniz: ")

        for x in range(10):
            print(settings.new_account(random_str(15) + "@gmail.com", passw))

        print("Bizi tercih ettiğiniz için teşekkürler, bütün hesaplar açıldı!")

    else:
        print("Lütfen tekrar gir")
        continue
