import smtplib
from datetime import datetime
from random import choice

from decouple import config

sender_adr = config('EMAIL')
sender_app_password = config('PASSWORD')
recipient_adr = config('RECIPIENT')


# make connection
def send_mail(message):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()  # to send messages encoded into net
        connection.login(user=sender_adr, password=sender_app_password)
        connection.sendmail(
            from_addr=sender_adr,
            to_addrs=recipient_adr,
            msg=f"Subject:Happy Birthday🎉\n\n{message}\nHappy Birthday to you 😊"
        )


with open(file="./quotes.txt", mode="r") as file:
    data = file.readlines()
    quotes_list = [quote.strip() for quote in data]


def send_mail_by_day():
    """checks date and choice random message to send by calling send mail"""
    day = 5
    if datetime.now().weekday() == day:
        MESSAGE = choice(quotes_list)
        send_mail(message=MESSAGE)
        print("Email Sent.")
    else:
        print("Error!")


send_mail_by_day()
