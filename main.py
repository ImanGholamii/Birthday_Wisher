import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from random import choice

from decouple import config
from pandas import read_csv

sender_adr = config('EMAIL')
sender_app_password = config('PASSWORD')
recipient_adr = ''


# make connection
def send_mail(message):
    """Create the email message using MIMEText with UTF-8 encoding"""
    msg = MIMEText(f"{message} 😊", 'plain', 'utf-8')
    msg['Subject'] = "Happy Birthday🎉"
    msg['From'] = sender_adr
    msg['To'] = recipient_adr

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()  # to send messages encoded into net
        connection.login(user=sender_adr, password=sender_app_password)
        connection.sendmail(
            from_addr=sender_adr,
            to_addrs=recipient_adr,
            msg=msg.as_string()
        )


with open(file="./quotes.txt", mode="r") as file:
    data = file.readlines()
    quotes_list = [quote.strip() for quote in data]

no_birth_day = False


def send_mail_by_day(data_list):
    """checks date and choice random message to send by calling send mail"""
    global recipient_adr, no_birth_day
    for data_tuple in data_list:
        if (datetime.now().day == datetime(data_tuple[1], data_tuple[2], data_tuple[3]).day and
                datetime.now().month == datetime(data_tuple[1], data_tuple[2], data_tuple[3]).month):
            index = data_tuple[0]
            name = birthdays_df.iloc[index]['name']
            number = choice([1, 2, 3])
            message = choice(quotes_list)
            recipient_adr = data_tuple[4]
            with open(file=f"letter_templates/letter_{number}.txt", mode="r") as letter_file:
                text = letter_file.readlines()
                new_text = [line.replace('[NAME]', name).replace("[message]", message) for line in text]
            try:
                os.mkdir("./sent_mails")  # to make sent_mails directory, automatically. You can Add it manually.
            except FileExistsError:
                pass
            except OSError as e:
                print(f"An error occurred while creating the directory: {e}")
            finally:
                with open(file=f"sent_mails/{name}_in_{datetime.now().year}.txt", mode="w") as output_file:
                    output_file.writelines(new_text)
            send_mail(message="".join(new_text))
            print(f"Email Sent to {name} Successfully.")
        else:
            no_birth_day = True

    if no_birth_day:
        print("You have not registered a birthday date associated with today's date.")


birthdays_df = read_csv("birthdays.csv")
birthday_data_list = [(index, row.year, row.month, row.day, row.email) for (index, row) in birthdays_df.iterrows()]


def main():
    send_mail_by_day(birthday_data_list)


if __name__ == '__main__':
    main()
