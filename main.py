#Monday Motivation Project

import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


# SMTP Sending Email with Python

# import smtplib

# my_email = "my_email@gmail.com"
# password = "passwordlkdfjbsdf"

# reciepient_address = "recpt_email@gmail.com"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=reciepient_address,
#                         msg="Ubject:Hello\n\nThis is the body of the email.")
#     connection.close()

# DATE TIME Working with date and time in Python

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# dayofweek = now.weekday()
# print(year)
#
# date_of_birth = dt.datetime(year=2003, month=7, day=5, hour=10)
# print(date_of_birth)