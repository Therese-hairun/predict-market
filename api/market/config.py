import csv
import os

MJ_APIKEY_PUBLIC = "7399050e847cbf60b38955194c6510aa"
MJ_APIKEY_PRIVATE = "9506a8890fd5398098c5a886454f6b0f"

TOKEN_MAX_AGE = 12
SMS_TOKEN = "46a35cddb2d444cbadc31e84dc114e4e"

MAIL_SENDER = "noreply@predictmarket.io"

with open("market/fakemail.csv", mode="r") as csvfile:
    JETTABLE_MAIL = []
    spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    for row in spamreader:
        data = row[0].split(",")[1].replace('"', "")
        JETTABLE_MAIL.append(data)

FAKE_MAIL = JETTABLE_MAIL
CODE_EXPIRATION_DAY = 1

FREE_DAYS = 1
CREDIT_PERCENT = 10

dbConfig = {
    "user": os.environ.get("DB_CRYPTO_USER"),
    "password": os.environ.get("DB_CRYPTO_PASSWORD"),
    "host": os.environ.get("DB_CRYPTO_HOST"),
    "database": os.environ.get("DB_CRYPTO_NAME"),
    "raise_on_warnings": True,
}

REMOVE_COUPLE_WAITING = 7
MAX_VUE = 3
TVA = 0.2
ATTEMPTED_LOGIN_MAIL_WAITING = 10
VUE_DAYS_INTERVAL = 7
SMS_SENT_WAITING_MINUTES = 1
