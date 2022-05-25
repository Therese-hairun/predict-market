from django.utils.translation import gettext
from market.settings import STRIPE_SECRET_KEY
from market.config import MAIL_SENDER, MJ_APIKEY_PRIVATE, MJ_APIKEY_PUBLIC
from .models import (
    ClientDowngrade,
    Invoice,
    Payment,
    Reward,
    Subscription,
)
from rest_framework import status

import datetime, mailjet_rest
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone, utc
import stripe

from predict.utils import format_amount
from .models import Client

stripe.api_key = STRIPE_SECRET_KEY


def start():
    scheduler = BackgroundScheduler(timezone=utc)
    scheduler.add_job(
        send_mail_subscription, "cron", day_of_week="mon-sun", hour="00", minute="00"
    )
    scheduler.add_job(
        renew_subscription, "cron", day_of_week="mon-sun", hour="00", minute="00"
    )
    scheduler.add_job(
        check_subscription, "cron", day_of_week="mon-sun", hour="00", minute="00"
    )
    scheduler.add_job(
        downgrade_subscription, "cron", day_of_week="mon-sun", hour="00", minute="00"
    )
    scheduler.start()


def send_mail_subscription():
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        if (
            subscription.end.replace(tzinfo=None)
            <= datetime.datetime.utcnow() - datetime.timedelta(weeks=1)
            and subscription.renew_status == True
        ):
            api_key = MJ_APIKEY_PUBLIC
            api_secret = MJ_APIKEY_PRIVATE
            mailjet = mailjet_rest.Client(auth=(api_key, api_secret), version="v3.1")
            subject = gettext("Subscription will expire")
            text = gettext("Your subscription will expire")
            message = gettext("Your subscription will expire on")
            data = {
                "Messages": [
                    {
                        "From": {"Email": f"{MAIL_SENDER}", "Name": "predict"},
                        "To": [
                            {
                                "Email": f"{subscription.client.email}",
                            }
                        ],
                        "Subject": subject,
                        "TextPart": text,
                        "HTMLPart": f"<h3>{message} : {subscription.end}</h3> ",
                    }
                ]
            }
            result = mailjet.send.create(data=data)
            if result.status_code != 200:
                print("Mail not sent")
            print("Mail sent")


def handle_price_amount(duration, price, reduction):
    if duration > 30:
        return (price - (price * (reduction / 100))) * 12
    else:
        return price


def renew_subscription():
    print(" ✅ ✅   inside renew_subscription")
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        print(
            """⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️
        subscription.subscribe.name = {}
        subscription.end={}
        datetime.datetime.utcnow = {}
        subscription.renew_status = {}
        subscription Client_id = {}
        ⬆️ ⬆️ ⬆️ ⬆️ ⬆️ ⬆️
        """.format(
                subscription.subscribe.name,
                subscription.end.replace(tzinfo=None),
                datetime.datetime.utcnow(),
                subscription.renew_status,
                subscription.client_id,
            )
        )

        if (
            subscription.subscribe.name != "Freemium"
            and subscription.end.replace(tzinfo=None) <= datetime.datetime.utcnow()
            and subscription.renew_status == True
        ):
            print(" ✅ ✅   inside IF renew_subscription")
            client = Client.objects.get(id=subscription.client.id)
            reward = Reward.objects.get(id=client.reward.id)
            customer = stripe.Customer.retrieve(client.customers_id)

            amount_subscription = handle_price_amount(
                subscription.duration,
                subscription.subscribe.price,
                subscription.subscribe.reduction,
            )
            amount = amount_subscription
            diff = amount - reward.total_for_next_subscription
            if diff >= 0:
                amount = diff
                reward.total_for_next_subscription = 0
            else:
                reward.total_for_next_subscription -= amount
                amount = 0
            reward.save()
            try:
                print(" 💶 💶   inside TRY auto-payment")
                payementResult = stripe.PaymentIntent.create(
                    amount=format_amount(amount),
                    currency="eur",
                    payment_method=subscription.payment_method_id,
                    customer=customer,
                    confirm=True,
                    receipt_email=client.email,
                )
                print(" 🎉 🎉 inside END TRY payment successful")
            except Exception as e:
                print("💥 💥 ERROR inside EXCEPTION === {}".format(e))

            subscription.start = datetime.datetime.utcnow()
            subscription.end = datetime.datetime.utcnow() + datetime.timedelta(
                days=subscription.duration
            )
            subscription.activate = True
            subscription.save()

            print(
                "➡️➡️ SUBSCRIPTION ACTIVATE STATUS = {} Client ID = {} ⬅️ ⬅️".format(
                    subscription.activate, subscription.client_id
                )
            )

            payment = Payment.objects.create(
                subscription=subscription,
                author=client.firstname + " " + client.lastname,
                created_at=datetime.datetime.utcnow(),
            )
            payment.reference = "PM" + "%06d" % payment.id
            payment.save()
            bill = Invoice.objects.create(
                payment=payment,
                initial_price=amount_subscription,
                discount_credit=amount_subscription - amount,
                discount_code=0,
                nb_crypto_currency=subscription.subscribe.number_couple_offered,
                created_at=datetime.datetime.utcnow(),
            )
            bill.final_price = bill.initial_price - (
                bill.discount_credit + bill.discount_code
            )
            bill.save()
            print(" ✅ ✅   inside end if renew_subscription")
    print(" ✅ ✅   inside end renew_subscription")


def check_subscription():
    print(" ✅ ✅   inside check_subscription")
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        if (
            subscription.subscribe.name != "Freemium"
            and subscription.end.replace(tzinfo=None) <= datetime.datetime.utcnow()
        ):
            print(" ✅ ✅  inside if check_subscription")
            subscription.activate = False
            subscription.save()
            print(" ✅ ✅  inside end if check_subscription")
    print(" ✅ ✅  inside end check_subscription")


def downgrade_subscription():
    client_downgrades = ClientDowngrade.objects.all()
    if client_downgrades.count() != 0:
        for client_downgrade in client_downgrades:
            if (
                client_downgrade.renew.replace(tzinfo=None)
                <= datetime.datetime.utcnow()
            ):
                print("------------- DOWNGRADE -----------------------")
                subscription = Subscription.objects.get(
                    client__id=client_downgrade.client.id
                )
                couples = client_downgrade.couples.all()
                if client_downgrade.couples.all().count() != 0:
                    item = [clientd.id for clientd in couples]
                    subscription.couples.set(item)
                subscription.subscribe = client_downgrade.subscribe
                subscription.duration = client_downgrade.duration
                subscription.start = datetime.datetime.utcnow()
                subscription.end = datetime.datetime.utcnow() + datetime.timedelta(
                    days=client_downgrade.duration
                )
                subscription.payment_method_id = client_downgrade.payment_method_id

                subscription.renew_status = False
                subscription.activate = True
                subscription.total_discount = client_downgrade.total_discount
                subscription.updated_at = datetime.datetime.utcnow()
                subscription.save()
                client_downgrade.delete()
