import random

kelimeler = {
    "kolay": ["araba", "kitap", "meyve", "kedi", "kalem", "masa", "köpek"],
    "orta": ["şemsiye", "sigara", "bardak", "tekerlek", "yazılım", "bilgisayar", "telefon"],
    "zor": ["radyoelektrik", "fizyoterapi", "simetrik", "organizasyon", "inovasyon", "kapitülasyon", "algoritma"]
}

seviye = input("Oyun seviyesini seçin (kolay/orta/zor): ")

while seviye not in kelimeler:
    seviye = input("Geçerli bir seviye seçin (kolay/orta/zor): ")


kelime_listesi = kelimeler[seviye]
kelime = random.choice(kelime_listesi)

isim = input("isminizi giriniz : ")
print("hoşgeldin " + isim + " oyuna başlıyoruz :)")
print(seviye + " seviyesini seçtin 10 yanlış tahmin hakkın vardır")


tahmin_string = ""

hak = 10 

while hak > 0:

    k_ekle = 0

    for karakter in kelime:
        if karakter in tahmin_string:
            print(karakter)
        else:
            print("-")
            k_ekle += 1
    if k_ekle == 0: 
        print("TEBRİKLER KAZANDIN :D Kelime "+ kelime )
        break

    tahmin = input("tahmin giriniz: " )
    tahmin_string += tahmin

    if tahmin not in kelime:
        hak -= 1 
        print("Yanlış tahmin !!!")
        print(f"{hak} hakkınız kaldı")
    if hak == 0: 
        print("kelime " + kelime +"'di oyunu kaybettiniz :( ")
