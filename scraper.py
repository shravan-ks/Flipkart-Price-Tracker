import smtplib
import time

import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": 'Your user agent'
}


def input_url():
    input_url = input('Paste Your Flipkart Product URL: ')
    # Splitting or slicing url to get website name i.e flipkart
    URL = input_url.split("//")[-1].split("/")[0]
    print(URL)
    if URL == 'www.flipkart.com':
        while True:
            check_price(URL)
            time.sleep(10)
    else:
        print("You Seem to Have Entered Wrong URL. Check If Your is From Flipkart.com")



def check_price(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(class_='_35KyD6').get_text()
    price = soup.find(class_='_1vC4OE _3qQ9m1').get_text()[1:]
    # strip_price = price[1:]
    convert_price = int(price.replace(',', ''))

    if convert_price < 12000:
        print(title)
        print(convert_price)
        send_mail(URL)
    else:
        print(title)
        print(convert_price)
        print("No Change in Price")


def send_mail(URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mail@gmail.com', 'mail-passowrd')

    subject = 'Price Fell Down !'
    body = f"Check the link {URL}"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'mail@gmail.com',
        'mail@gmail.com',
        msg
    )
    print('Mail Has Been Sent !')
    server.quit()

