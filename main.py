import smtplib
from datetime import datetime
from random import choice

from decouple import config
from pandas import read_csv

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


def send_mail_by_day(date_list):
    """checks date and choice random message to send by calling send mail"""
    for date in date_list:
        if datetime.now().weekday() == date[1] and datetime.now().month == date[0]:
            file = choice([1, 2, 3])
            MESSAGE = choice(quotes_list)
            with open(file=f"letter_templates/letter_{file}.txt", mode="r") as file:
                text = file.readlines()
                new_text = [line.replace('[NAME]', birthdays_df.name).replace("[message]", MESSAGE) for line in text if
                 '[NAME]' in line or '[message]' in line]
            with open(file=f"{birthdays_df.name}_in_{datetime.now().year}.txt", mode="w") as output_file:
                output_file.writelines(new_text)
                print(output_file)
            # send_mail(message=output_file)
            print("Email Sent Successfully.")
        else:
            print("Error!\nunable to send mail.")


birthdays_df = read_csv("birthdays.csv")
dates = [(row.month, row.day) for (index, row) in birthdays_df.iterrows()]

send_mail_by_day(date_list=dates)
