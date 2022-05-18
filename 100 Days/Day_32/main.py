##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
from random import choice
import smtplib

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
this_month = now.month
this_day = now.day

my_email_yahoo = "mikhailpitsukov@yahoo.com"
my_email_gmail = "mikhailpitsukov@gmail.com"
password_gmail = "St9%Rga17#"
password_yahoo = "pexxbmoqiwhivrwo"

for _ in range(len(df)):
    if this_day == df.loc[_, "day"] and this_month == df.loc[_, "month"]:
        random_letter = choice(["letter_1", "letter_2", "letter_3"])
        with open(f"letter_templates/{random_letter}.txt", "r") as letter:
            text = letter.read()
            message = text.replace("[NAME]", df.loc[_, 'name'])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email_gmail, password=password_gmail)
                connection.sendmail(from_addr=my_email_gmail, to_addrs=df.loc[_, "email"],
                                    msg=f"Subject:Test BD sending\n\n{message}")










