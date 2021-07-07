import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.in/New-Apple-iPhone-Mini-64GB/dp/B08L5VDDQ5/ref=sr_1_1_sspa?crid=3EM5S05AFKMFE&dchild=1&keywords=iphone+12+mini&qid=1625208103&sprefix=iphone+12%2Caps%2C328&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFKWlRXMkc5VTdXWVAmZW5jcnlwdGVkSWQ9QTA0MjYzOTEyU09OM1BFVTFXODdSJmVuY3J5cHRlZEFkSWQ9QTAzMjM3ODgzNjRQMURZOUtRWlNMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()
    price= soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[2:8]
    final_price = int(converted_price.replace(",",""))
    print(title.strip())
    print(price.strip())

    if(final_price<60000):
        send_mail()
    else:
        print(str(final_price) +" is Higher")
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('example@gmail.com','password')

    subject = "Price fell down"
    body = f"Check the Amazon link, "+ URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'charanhv2000@gmail.com',
        'charanhv852000@gmail.com',
        msg
    )
    print('Email has been SENT!')

    server.quit()

check_price()