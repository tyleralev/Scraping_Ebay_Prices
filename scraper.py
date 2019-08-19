import requests
from bs4 import BeautifulSoup
import smtplib
import re
import time

URL = 'https://www.ebay.com/itm/2014-Triumph-Bonneville/183919270176?hash=item2ad2715920:g:CU4AAOSwhBBdO2y4'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum_bidPrice").get_text()
    converted_price = float(re.sub(r'[^0-9\.]', '', price))

    if(converted_price < 5000.00):
        send_mail()

    print(title)
    print(converted_price)

    if(converted_price > 5000.00):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('talev21@gmail.com', 'nqiwnrcqpinserde')

    subject = 'Price fell down!'
    body = 'CHECK THE LINK' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'talev21@gmail.com',
        'lukehuerta24@gmail.com',
        msg
    )

    print('Message was sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60*24)
