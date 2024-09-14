import smtplib
from decouple import config
from random import choice

sender_adr = config('EMAIL')
sender_app_password = config('PASSWORD')
recipient_adr = config('RECIPIENT')

# make connection
def send_mail():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()  # to send messages encoded into net
        connection.login(user=sender_adr, password=sender_app_password)
        connection.sendmail(
            from_addr=sender_adr,
            to_addrs=recipient_adr,
            msg="Subject:Iman_Gholami\n\nthat was changes to subject and here is body."
            )


with open(file="./quotes.txt", mode="r") as file:
    data = file.readlines()
    quotes_list = [quote.strip() for quote in data]

print(choice(quotes_list))
