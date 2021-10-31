import requests
from bs4 import BeautifulSoup

header = {'User-agent': 'Mozilla/5.0'}

link = input("Link:")

r = requests.get(link, headers=header)
soup = BeautifulSoup(r.content, "lxml")

urunad = soup.find("header", {"class": "title-wrapper"}).find("span").text

indirim_yüzdesi = soup.find("div", {"class": "active"}).find(
    "span").text.strip().strip("indirim").strip()

şuanki_fiyat = soup.find("div", {"class": "extra-discount-price"}).text.strip()

ozellikler = soup.find(
    "div", {"id": "productTechSpecContainer"}).find_all("tr")

print("Ürün Adı -> ", urunad)
print("Şuanki Fiyatı -> ", şuanki_fiyat)
print("↓ Ürün Özellikleri ↓")
print("------------------")

for detay in ozellikler:
    etiket = detay.find("th").text
    deger = detay.find("td").text
    print(etiket, " = ", deger)
