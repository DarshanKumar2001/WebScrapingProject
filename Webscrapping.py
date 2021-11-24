import requests
from bs4 import BeautifulSoup
#URL='https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HG8S7KP/ref=sr_1_1?keywords=m31&qid=1637577739&qsid=257-3591481-4383748&sr=8-1&sres=B07HG8S7KP%2CB07HGLM366%2CB08X4XW41P%2CB09CGJK2HG%2CB09J2HZQZH%2CB08ZJRRLKC%2CB096VD213D%2CB096LRGL64%2CB098NFJXXL%2CB098NGDNMT%2CB098NHMPJJ%2CB096VD6RQG%2CB08XGDN3TZ%2CB096LS7N6Z%2CB08444SXZ6%2CB08XJG8MQM&srpt=CELLULAR_PHONE'
#URL='https://www.amazon.in/Samsung-Charcoal-Storage-Replacement-SM-M215GZKDINS/dp/B098NFJXXL/ref=sr_1_1_sspa?keywords=m21&qid=1637583751&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4WVk0WFE2TVlWVFgmZW5jcnlwdGVkSWQ9QTAyMTY2MTAyTU9OQ05WMlg3MFVHJmVuY3J5cHRlZEFkSWQ9QTA1NzE4ODZTQTlBTzlaMFZaMkImd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
product_to_track = [
    {
        "URL": "https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGLM366/ref=sr_1_1?keywords=m31&qid=1637578855&qsid=257-3591481-4383748&sr=8-1&sres=B07HGLM366%2CB08X4XW41P%2CB09CGJK2HG%2CB09J2HZQZH%2CB08ZJRRLKC%2CB096VD213D%2CB096LRGL64%2CB098NFJXXL%2CB098NGDNMT%2CB098NHMPJJ%2CB096VD6RQG%2CB08XGDN3TZ%2CB09GFMFTHS%2CB096LS7N6Z%2CB08444SXZ6%2CB08XJG8MQM&srpt=CELLULAR_PHONE",
        "name":"Samsung Galaxy M31 Space Black, 8GB RAM, 128GB Storage",
        "target_prize":15000
    },
    {
        "URL":"https://www.amazon.in/Samsung-Charcoal-Storage-Replacement-SM-M215GZKDINS/dp/B098NFJXXL/ref=sr_1_1_sspa?keywords=m21&qid=1637583751&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4WVk0WFE2TVlWVFgmZW5jcnlwdGVkSWQ9QTAyMTY2MTAyTU9OQ05WMlg3MFVHJmVuY3J5cHRlZEFkSWQ9QTA1NzE4ODZTQTlBTzlaMFZaMkImd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl",
        "name":"Samsung Galaxy M21 2021 Edition Charcoal Black, 4GB RAM, 64GB Storage ",
        "target_prize":14000
    },
    {
        "URL":"https://www.amazon.in/Redmi-Note-10T-5G-Dimensity/dp/B097YF6BXF/ref=sr_1_1?crid=1S4NAWW7EUUVJ&keywords=redmi+note+10t+5g&qid=1637588922&qsid=262-8534365-9973050&sprefix=redmi+not%2Caps%2C649&sr=8-1&sres=B097YF6BXF%2CB09C883CQR%2CB09H5RF5YH%2CB0948NFSWX%2CB09C6BPT7L%2CB09CGKJKQ9%2CB08LRDM44F%2CB09CGJFY5N%2CB09CGJK2HG%2CB0948NNY3W%2CB09CTZ1WFP%2CB08444SXZ6%2CB09CTZ1Z75%2CB089MSPF7Q%2CB08VB34KJ1%2CB09CTYGJSD&srpt=NOTEBOOK_COMPUTER",
        "name":"Redmi Note 10T 5G Graphite Black, 6GB RAM, 128GB Storage",
        "target_prize":17000
    },
    {
        "URL": "https://www.amazon.in/Oppo-Mystery-Storage-Additional-Exchange/dp/B08444S68L/ref=sr_1_1?crid=3PCZGHWTWOX9H&keywords=oppo+a31+6+128+mobile+phone&qid=1637589064&qsid=262-8534365-9973050&sprefix=oppo%2Caps%2C813&sr=8-1&sres=B08444S68L%2CB08444SXZ6%2CB08444XVNP%2CB089MV4H2W%2CB0844592HB%2CB099SJ233B%2CB09DWZH73K%2CB08VB34KJ1%2CB08444SW5Z%2CB099SJHHQL%2CB08VB2CMR3%2CB09FKDB27R%2CB09FKD67CS%2CB09FKCGP9T%2CB09FKB3446%2CB09FK8MBMJ&srpt=CELLULAR_PHONE",
        "name": "OPPO A31 Mystery Black, 6GB RAM, 128GB Storage",
        "target_prize": 13000
    },
    {
        "URL": "https://www.amazon.in/realme-narzo-Racing-Sliver-Storage/dp/B099SF5X1W/ref=sr_1_2?keywords=realme&qid=1637589140&qsid=262-8534365-9973050&sr=8-2&sres=B099SJHHQL%2CB099SF5X1W%2CB09FKB3446%2CB09FKDB27R%2CB09FK8MBMJ%2CB09FKDH6FS%2CB09FKD67CS%2CB09FKGDJNC%2CB09FKCGP9T%2CB09LQ8YS6T%2CB094Y495LQ%2CB07XMFDHSG%2CB0999NNBPV%2CB0999NDRFC%2CB08225158Y%2CB097KMXXTZ&srpt=CELLULAR_PHONE",
        "name": "realme narzo 30 (Racing Sliver, 6GB RAM, 128GB Storage",
        "target_prize": 16000
    },
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")
    return product_price.getText()

result_file=open('WebScrapping_file.txt','w')
try:
    for every_product in product_to_track:
        product_prize_returned = give_product_price(every_product.get("URL"))
        print(product_prize_returned + "-" + every_product.get("name"))

        my_product_prize = product_prize_returned[1:]
        my_product_prize = my_product_prize.replace(',', '')
        my_product_prize = float(my_product_prize)
        if my_product_prize < every_product.get("target_prize"):
            print("Available at best prize")
            result_file.write(every_product.get("name") + '-' + ' available_at_best_prize\n' + 'Current Prize - ' + str(my_product_prize) +'\n')
        else:
            print("Still at current prize")
finally:
    result_file.close()


