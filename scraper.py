import smtplib
import time
import re 
import requests
from bs4 import BeautifulSoup
from avatar import avatar

headers = {
    "User-Agent": 'Your user agent'
}


class Main:
    def __init__(self):
        avatar()
        # get email - password and to email
        self.email = input('Enter Your Email : ')
        self.password = input('Enter your email password ,  **Note your password is stored locally on your system** : ')
        self.to_email = input('Email Address that you want to get alert , LEAVE BLANK if ' + self.email + ' : ' ) or self.email
        # for validating an Email 
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        # validating an Email 
        # and the string in search() method 
        if  re.search(regex,self.email) and re.search(regex, self.to_email):
            print('*' * 150)  
            print("Email Register... done!")
            print('*' * 150)
            # call get url function
            self.get_url()
        else:
            print('-' * 150)    
            print("Invalid Email, Try Again !")
            print('-' * 150)
            # if invalid email re-run init() 
            self.__init__()

    def get_url(self):
        # get URL
        self.url = input('Paste Your Flipkart Product URL: ')
        # Splitting or slicing url to get website name i.e flipkart
        check_url = self.url.split("//")[-1].split("/")[0]
        # check if url belongs to Flipkart
        if check_url == 'www.flipkart.com':
            time.sleep(3)
            print('*' * 150)
            # get wished price  
            self.wished_price = int(input("Enter the price to track, i.e desired less of your product: ₹"))
            print('~' * 150)  
            self.check_price()
        else:
            print('-' * 150)  
            print(" You Seem to Have Entered Wrong URL. Check If Your is From Flipkart.com")
            print('-' * 150)  
            time.sleep(3)
            # if wrong url re-run get_url() 
            self.get_url()

    # check price
    def check_price(self):
        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        # validate url page if item exists
        try:
            self.title = soup.find(class_='_35KyD6').get_text()
            raw_price = soup.find(class_='_1vC4OE _3qQ9m1').get_text()[1:]
        except:
            print('~' * 150)  
            print('Error with URL , Copy Correct URL, Try Again !!')
            print('~' * 150)  
            self.get_url()
        # strip_price = price[1:]
        self.price = int(raw_price.replace(',', ''))
        
        print('Product Name: ₹', self.title)
        print('Product Flipkart Price: ₹',self.price)
        print('Product Wished Price: ₹',self.wished_price)
        
        # compare
        if self.wished_price < self.price :
            print("No Change in Price")
            print('~' * 150)
            time.sleep(10)
            # check again after a while
            self.check_price()
        else:
            # price less
            print('*' * 150)
            print('Hurray ! Seems like the price of ' + self.title + 'has fell down, Right Time to Order now \n\n' 'Click this link : : ' + self.url )
            print('*' * 150)
            time.sleep(3)
            self.send_mail()
        
    # send mail
    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(self.email, self.password)

        subject = 'Price Fell Down !'
        body = f"Check the link \n {self.url}"

        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            self.email,
            self.to_email,
            msg
        )
        print('Mail Has Been Sent !')
        print('~' * 150)
        server.quit()

# call Class 
Main()