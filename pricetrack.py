import requests #used to send a request to and from the URL to get the price data we need
from bs4 import BeautifulSoup #used to scrape the HTML code from the website to find the price and title of the product
import time #to ensure it checksd wevery few seconds and doesnt keep on pinging the website
import smtplib #to enable python to send an email using your email client

URL1="target product URL"
 #User-Agent value can be found by searching "my user agent" on google and it returns the value. paste below
HEADERS = {"User-Agent":"add user ID here"}

#target prices
priceof1 = 123

#Email Login Details
email_address="youremailaddress" #the code will send you a email from yourself if the price drops below your requirement
password="youraccountpassword" #since it needs to login as you in order to send the email

def track_price():
    price=int(getprice())
    if price>priceof1:
        diff=price-priceof1
        print(f"It's still {diff} too expensive")
    else:
        print("Cheaper")
        sendmail()

def sendmail():
    subject = "Amazon Price has dropped"
    mailtext = "Subject:"+subject+'\n\n'+URL1

    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(email_address,password)
    server.sendmail(email_address, email_address, mailtext)
    pass

def getprice():
    page1 = requests.get(URL1, headers=HEADERS)
    soup = BeautifulSoup(page1.content, 'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()[2:4]
    print(title)
    print(price)
    return price

if __name__ == "__main__":
    while True:
        track_price()
        time.sleep(120) #time in Seconds for gap between two consecutive checks
