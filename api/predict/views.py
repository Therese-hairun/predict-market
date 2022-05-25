import json, jwt, datetime, requests, mailjet_rest, os
import math

from django.utils.translation import gettext
from django.db.models.aggregates import Max
from django import db
from requests.models import encode_multipart_formdata
import rest_framework
from market.settings import STRIPE_SECRET_KEY, PARM_INTERVAL
from predict import auth
from predict.auth import AdminAuthentication
from predict.constant import (
    ASSET_NOT_FOUND,
    CLIENT_NOT_FOUND,
    COUPLE_NOT_FOUND,
    DEFAULT_MAIL,
    DELETE_SUCCESSFUL,
    ERROR_DB_CONNECT,
    FAVORITE_NOT_FOUND,
    LINKEDIN_API_URL,
    LINKEDIN_AUTH_LINK,
    REWARD_NOT_FOUND,
    SUBSCRIBE_NOT_FOUND,
    TICKET_NOT_FOUND,
    TOKEN_EXPIRED,
    UPDATE_SUCCESSFUL,
    LOCALHOST_IP,
)
from predict.pagination import (
    CouplePageNumberPagination,
    InvoicePageNumberPagination,
    ReductionCodePageNumberPagination,
    SubscribePageNumberPagination,
    ClientPageNumberPagination,
    RewardPageNumberPagination,
    LogPageNumberPagination,
)
from market.config import (
    ATTEMPTED_LOGIN_MAIL_WAITING,
    FREE_DAYS,
    MAIL_SENDER,
    MAX_VUE,
    MJ_APIKEY_PRIVATE,
    MJ_APIKEY_PUBLIC,
    REMOVE_COUPLE_WAITING,
    SMS_SENT_WAITING_MINUTES,
    SMS_TOKEN,
    VUE_DAYS_INTERVAL,
    dbConfig,
)
from predict.text import ATTEMPT_LOGIN, ATTEMPT_LOGIN_ACCOUNT
from predict.utils import (
    dict2obj,
    fakemail,
    find_first_interval,
    format_amount,
    format_h24,
    format_interval,
    generate_token,
    get_credit_percentage,
    get_precision,
    get_request_token,
    get_training_state,
    make_filter_interval,
    replaceTextBetween,
    round_minutes,
    round_time,
    sort_interval,
    substract_time,
    to_timestamp_milliseconds,
    validate_password,
)
from prediction.models import Asset, Symbol, Training
from django.contrib.auth.hashers import make_password, check_password
from .serializers import (
    AdminSerializer,
    ClientByTokenSerializer,
    ClientRewardSerializer,
    ClientSerializer,
    CodeReductionAvailableSerializer,
    CoupleFavoriteInfoSerializer,
    CoupleInfoSerializer,
    CoupleVueSerializer,
    CreateTicketMessageSerializer,
    CreateTicketSerializer,
    InvoiceSerializer,
    SubcribeSerializer,
    SubscriptionCreateSerializer,
    SubscriptionSerializer,
    RewardSerializer,
    SubscriptionWithEmailSerializer,
    CoupleSerializer,
    CoupleDemandSerializer,
    CoupleFavoriteSerializer,
    CoupleAuthorisedSerializer,
    TicketMessageSerializer,
    TicketSerializer,
    ApiLogsSeralizer,
)

from .models import (
    SMS,
    Admin,
    Client,
    ClientDowngrade,
    ClientPhone,
    ClientToken,
    CodeReductionAvailable,
    CodeReductionUsed,
    CoupleAuthorized,
    CoupleData,
    CoupleDemand,
    CoupleFavorite,
    CoupleHistory,
    CoupleVue,
    Invoice,
    Payment,
    SimpleRewardByRelationshipCode,
    Subscribe,
    Subscription,
    Reward,
    Couple,
    Ticket,
    TicketMessage,
)

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from django import db
import stripe
from django.db.models import Count
import mysql.connector
from django.core.paginator import Paginator

from predict import models
from calendar import monthrange
import arrow
from django.utils import translation
from drf_api_logger.models import APILogsModel

# GET ALL CLIENT
@api_view(["GET"])
def user_list(request):
    clients = Client.objects.all().order_by("-id")
    print(clients.id)
    serializer = ClientSerializer(clients, many=True)

    return Response(serializer.data)


# GET CLIENT INFORMATION
@api_view(["GET"])
def get_client(request):
    pk = jwt.decode(
        get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
    )
    try:
        client = Client.objects.get(id=pk["id"])
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    serializer = ClientByTokenSerializer(
        client, many=False, context={"request": request}
    )
    return Response(serializer.data)


# CREATE CLIENT
@api_view(["POST"])
@authentication_classes([])
def create_client(request):
    if bool(request.data) is not False:
        reward = Reward.objects.create(
            sum=0,
            free_day=0,
            created_at=datetime.datetime.utcnow(),
            total_for_next_subscription=0,
        )
        reward.save()
        next_id = Client.objects.count() + 1
        request.data["password"] = make_password(request.data["password"])
        request.data["email"] = str(next_id) + request.data["email"]
        request.data.update(
            {"created_at": datetime.datetime.utcnow(), "reward": reward.id}
        )
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            client = Client.objects.get(id=serializer.data["id"])
            phone = ClientPhone.objects.create(
                client=client,
                number=client.phone,
                is_phone_active=True,
                created_at=datetime.datetime.utcnow(),
            )
            token = generate_token(client.id)
            client.token = token.get("token")
            clientToken = ClientToken.objects.create(
                client=client,
                token=token.get("token"),
                created_at=datetime.datetime.utcnow(),
                token_expiry=token.get("exp"),
            )
            client.save()
            clientToken.save()
            phone.save()

            return Response({"id": serializer.data["id"]})
        else:

            print(serializer.errors)
            if "phone" in serializer.errors:
                return Response(
                    {"Message": "Ce numéro de téléphone est déjà utilisé!"},
                    status=status.HTTP_409_CONFLICT,
                )
            elif "storage_code_client" in serializer.errors:
                return Response(
                    {"Message": "Ce code est déjà utilisé!"},
                    status=status.HTTP_409_CONFLICT,
                )
    else:
        return Response({"Error": "Error no data"}, status=status.HTTP_400_BAD_REQUEST)


# CLIENT LOGIN
@api_view(["POST"])
@authentication_classes([])
def login(request):
    if "language" in request.query_params:
        language = request.query_params["language"]
        if language in ["fr", "en"]:
            if language == "fr":
                translation.activate(language)
            if language == "en":
                translation.activate(language)
    try:
        superUser = Admin.objects.get(email=request.data["email"])
    except Admin.DoesNotExist:
        client = Client.objects.filter(
            email=request.data["email"],
        ).first()
        if client is None:
            print(CLIENT_NOT_FOUND)
            return Response(
                {"Error": CLIENT_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST
            )
        if not check_password(request.data["password"], client.password):
            if client.login_attempted_error is None or datetime.datetime.now() > (
                client.login_attempted_error.replace(tzinfo=None)
                + datetime.timedelta(minutes=ATTEMPTED_LOGIN_MAIL_WAITING)
            ):
                api_key = MJ_APIKEY_PUBLIC
                api_secret = MJ_APIKEY_PRIVATE
                mailjet = mailjet_rest.Client(
                    auth=(api_key, api_secret), version="v3.1"
                )
                hello = gettext("Hello")
                msg = gettext("We have detected a login attempt on your account on")
                data = {
                    "Messages": [
                        {
                            "From": {"Email": f"{MAIL_SENDER}", "Name": "predict"},
                            "To": [
                                {
                                    "Email": f'{request.data["email"]}',
                                }
                            ],
                            "Subject": gettext("Attempting to connect"),
                            "TextPart": gettext("Attempting to log into your account"),
                            "HTMLPart": f"<h3>{hello} {client.lastname},</h3></br><h3>{msg} :</h3></br> {datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')} ",
                        }
                    ]
                }
                result = mailjet.send.create(data=data)
                if result.status_code != 200:
                    print("Mail not sent")
                print("Mail sent")
                client.login_attempted_error = datetime.datetime.now()
                client.save()
            return Response(
                {"Error": CLIENT_NOT_FOUND},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if client.account_is_active:
            token = generate_token(client.id)
            client.token = token.get("token")
            clientToken = ClientToken.objects.get(client=client)
            clientToken.token = token.get("token")
            clientToken.updated_at = datetime.datetime.utcnow()
            clientToken.token_expiry = token.get("exp")
            client.save()
            clientToken.save()
            print("Login successful")

            return Response(
                {
                    "token": token.get("token"),
                }
            )

        return Response({"Error": "Compte non activé"}, status=status.HTTP_423_LOCKED)
    print("Admin login successful")
    if check_password(request.data["password"], superUser.password):
        adminToken = generate_token(superUser.id, True)
        superUser.token = adminToken.get("token")
        superUser.save()
        return Response({"adminToken": adminToken.get("token")})
    return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)


# SEND  VERIFICATION MAIL TO CLIENT
@api_view(["POST"])
@authentication_classes([])
def send_mail(request):
    if "language" in request.query_params:
        language = request.query_params["language"]
        if language in ["fr", "en"]:
            if language == "fr":
                translation.activate(language)
            if language == "en":
                translation.activate(language)
    if fakemail(request.data["email"]):
        print("Fake mail not acceptable")

        return Response(
            {"Message": "Fake mail not acceptable"},
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
    try:
        client = Client.objects.get(id=request.data["id"])
    except Client.DoesNotExist:
        print(CLIENT_NOT_FOUND)

        return Response(
            {"Message": CLIENT_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        client.email = request.data["email"]
        client.save()
    except db.IntegrityError:

        return Response(
            {"Message": "L'adresse Email existe déjà "}, status=status.HTTP_409_CONFLICT
        )
    api_key = MJ_APIKEY_PUBLIC
    api_secret = MJ_APIKEY_PRIVATE
    mailjet = mailjet_rest.Client(auth=(api_key, api_secret), version="v3.1")
    here = gettext("Here is your")
    msg = gettext("verification link")
    data = {
        "Messages": [
            {
                "From": {"Email": f"{MAIL_SENDER}", "Name": "predict"},
                "To": [
                    {
                        "Email": f'{request.data["email"]}',
                    }
                ],
                "Subject": gettext("Verification link"),
                "TextPart": gettext("Here is your verification link"),
                "HTMLPart": f"<h3>{here} <a href='{ os.environ.get('FRONT_URL') or 'http://localhost:8080'}/#/felicitation/{generate_token(client.id)['token']}'>{msg}</a> </h3> ",
            }
        ]
    }
    result = mailjet.send.create(data=data)
    if result.status_code != 200:
        print("Mail not sent")

        return Response({"state": "Email non envoyé"})
    print("Mail sent")

    return Response({"state": "Email envoyé avec succès"})


# SEND VERIFICATION CODE SMS
@api_view(["POST"])
@authentication_classes([])
def send_sms(request):
    last_sms = SMS.objects.filter(
        number=request.data["To"], sender_ip=request.META.get("REMOTE_ADDR")
    ).last()
    if last_sms is None or (
        (
            last_sms.send_at.replace(tzinfo=None)
            + datetime.timedelta(minutes=SMS_SENT_WAITING_MINUTES)
        )
        <= datetime.datetime.utcnow()
    ):
        token = SMS_TOKEN
        reqUrl = "https://api.mailjet.com/v4/sms-send"
        headers = {"Authorization": "Bearer " + token}
        data = json.dumps(request.data, sort_keys=True, indent=4)
        response = requests.request("POST", reqUrl, data=data, headers=headers)
        if response.status_code != 200:
            print("SMS not sent")
            return Response(
                {"State": "SMS not sent", "Error": response.json()["ErrorMessage"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        print("SMS sent")
        client = Client.objects.get(phone=request.data["To"])
        phone = ClientPhone.objects.get(number=request.data["To"])
        phone.sms_code = client.sms_validation_code
        phone.sms_date = datetime.datetime.utcnow()
        phone.save()
        sms = SMS.objects.create(
            sender_ip=request.META.get("REMOTE_ADDR"), number=request.data["To"]
        )
        sms.save()
        return Response({"status": "SMS sent"})
    else:
        return Response(
            {"Error": "Please wait before sending another sms"},
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )


# SEND LINK MAIL TO RESET PASSWORD
@api_view(["POST"])
@authentication_classes([])
def reset_password(request):
    if "language" in request.query_params:
        language = request.query_params["language"]
        if language in ["fr", "en"]:
            if language == "fr":
                translation.activate(language)
            if language == "en":
                translation.activate(language)

    try:
        user = Client.objects.get(email=request.data["email"])
    except Client.DoesNotExist:
        print(CLIENT_NOT_FOUND)

        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
    client_user = (ClientSerializer(instance=user)).data
    api_key = MJ_APIKEY_PUBLIC
    api_secret = MJ_APIKEY_PRIVATE
    mailjet = mailjet_rest.Client(auth=(api_key, api_secret), version="v3.1")
    hello = gettext("Hello")
    here = gettext("Here is your")
    msg = gettext("password reset link")
    data = {
        "Messages": [
            {
                "From": {"Email": f"{MAIL_SENDER}", "Name": "predict"},
                "To": [{"Email": f"{user.email}", "Name": f"{user.lastname}"}],
                "Subject": gettext("Reset password"),
                "TextPart": gettext("Reset link"),
                "HTMLPart": f'<h3>{hello} {client_user["firstname"] } ,</h3><h3>{here} <a href="{os.environ.get("FRONT_URL") or "http://localhost:8080"}/#/reinitialisation/{generate_token(client_user["id"])["token"]}">{msg}</a></h3>',
            }
        ]
    }
    result = mailjet.send.create(data=data)
    if result.status_code != 200:
        print("Mail not sent")

        return Response({"State": "Email non envoyé"})
    print("Mail sent")

    return Response({"State": "Email envoyé"})


# RESET PASSWORD (UPDATE)
@api_view(["PATCH"])
def update_password(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:

        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        print(CLIENT_NOT_FOUND)

        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
    if validate_password(request.data["password"]):
        client.password = make_password(request.data["password"])
        client.save()
        print("Reset password successful")

        return Response({"Message": "Reset password successful"})
    return Response(
        {"Error": "Invalid password format"}, status=status.HTTP_400_BAD_REQUEST
    )


####
# CHANGE CUSTOMER ACCOUNT STATUS FROM VUEJS
#
# #####


@api_view(["PUT"])
@authentication_classes([AdminAuthentication])
def change_cusomer_status(request, id):
    client = Client.objects.get(id=id)

    client.account_is_active = request.data["account_is_active"]
    client.save()

    return Response({"State": "Status updated"})


# ADD SUBSCRIBE
@api_view(["POST"])
@authentication_classes([AdminAuthentication])
def add_subscribe(request):
    if {"name", "price", "reduction", "number_couple_offered"} <= request.data.keys():
        request.data.update({"created_at": datetime.datetime.utcnow()})
        serializer = SubcribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {"Status": "Subscription created successfully", "data": serializer.data}
            )
        print("Error", serializer.errors)
        return Response(
            {"Error": "Subscription not created"}, status=status.HTTP_404_NOT_FOUND
        )
    return Response(
        {"Error": "Subscription data error"}, status=status.HTTP_400_BAD_REQUEST
    )


# GET ALL SUBSCRIBE
class ApiSubscribeListView(ListAPIView):
    queryset = Subscribe.objects.exclude(name="Freemium")
    serializer_class = SubcribeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name",)
    ordering_fields = "__all__"
    pagination_class = SubscribePageNumberPagination


# GET SUBCRIBE BY ID
@api_view(["GET"])
def get_by_subscribe_id(request, id):
    try:
        subscribe = Subscribe.objects.get(id=id)
    except Subscribe.DoesNotExist:

        return Response(
            {"Error": SUBSCRIBE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = SubcribeSerializer(subscribe, many=False)

    return Response(
        {"Status": "Get subscribe info successfull", "data": serializer.data}
    )


# UPDATE SUBCRIBE
@api_view(["PATCH"])
@authentication_classes([AdminAuthentication])
def update_subscribe(request, id):
    try:
        subscribe = Subscribe.objects.get(id=id)
    except Subscribe.DoesNotExist:
        print(SUBSCRIBE_NOT_FOUND)

        return Response(
            {"Error": SUBSCRIBE_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST
        )
    request.data.update(
        {"created_at": subscribe.created_at, "updated_at": datetime.datetime.utcnow()}
    )
    serializer = SubcribeSerializer(subscribe, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response({"Status": UPDATE_SUCCESSFUL, "data": serializer.data})
    print("Error: ", serializer.errors)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  UPDATE SUBSCRIBE STATUS
@api_view(["PUT"])
@authentication_classes([AdminAuthentication])
def update_subscribe_status(request, id):
    try:
        subscribe = Subscribe.objects.get(id=id)
    except Subscribe.DoesNotExist:
        print(SUBSCRIBE_NOT_FOUND)
        return Response(
            {"Error": SUBSCRIBE_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST
        )
    subscribe.is_active = request.data["is_active"]
    subscribe.save()
    print(UPDATE_SUCCESSFUL)

    return Response({"Status": UPDATE_SUCCESSFUL})


# UPDATE SUBSCRIBE RECOMMANDED
@api_view(["PUT"])
@authentication_classes([AdminAuthentication])
def update_subscribe_recommanded(request, id):
    try:
        subscribe = Subscribe.objects.get(id=id)
        subscribes = Subscribe.objects.exclude(id=id)
    except Subscribe.DoesNotExist:
        print(SUBSCRIBE_NOT_FOUND)
        return Response(
            {"Error": SUBSCRIBE_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST
        )
    subscribes.update(recommanded=False)
    subscribe.recommanded = request.data["recommanded"]
    subscribe.save()

    print(UPDATE_SUCCESSFUL)

    return Response({"Status": UPDATE_SUCCESSFUL})


# UPDATE PHONE STATUS


@api_view(["PATCH"])
@authentication_classes([])
def update_phone_status(request):
    try:
        client = Client.objects.get(
            phone=request.data["phone"], sms_validation_code=request.data["code"]
        )
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    client.phone_is_activated = True
    client.save()
    return Response({"Status": "Phone activated"})


# UPDATE EMAIL STATUS


@api_view(["PATCH"])
def update_email_status(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:

        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        Subscription.objects.get(client=client)
    except Subscription.DoesNotExist:
        client.email_is_activated = True
        client.account_is_active = True
        subscribe, created = Subscribe.objects.get_or_create(
            name="Freemium",
            created_at=datetime.datetime.utcfromtimestamp(10000),
            price=0,
            reduction=0,
            number_couple_offered=2,
        )
        if created:
            subscribe.save()
        subscription = Subscription.objects.create(
            client=client,
            subscribe=subscribe,
            duration=30,
            start=datetime.datetime.utcnow(),
            end=datetime.datetime.utcnow() + datetime.timedelta(days=30),
            renew_status=0,
            total_discount=0,
            created_at=datetime.datetime.utcnow(),
            activate=True,
        )
        subscription.save()
        client.save()
        if client.relationship_code:
            clientReward = SimpleRewardByRelationshipCode.objects.create(
                client_child_name=client,
                reward_day_by_child=FREE_DAYS,
                reward_credit_by_child=0.0,
                created_at=datetime.datetime.utcnow(),
            )
            clientReward.save()
            parrain = Client.objects.get(storage_code_client=client.relationship_code)
            parrainReward = Reward.objects.get(id=parrain.reward.id)
            parrainReward.free_day = parrainReward.free_day + FREE_DAYS
            parrainReward.save()
        return Response({"Status": "Email activated"})
    return Response(
        {"Error": "Client already have a subscription"}, status=status.HTTP_409_CONFLICT
    )


# UPDATE CLIENT GENERAL INFO


@api_view(["PATCH"])
def update_client_general_info(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:

        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:

        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    if (
        request.data["firstname"].strip().__len__() == 0
        or request.data["lastname"].strip().__len__() == 0
    ):
        return Response({"Error": "Data error"}, status=status.HTTP_400_BAD_REQUEST)
    client.firstname = request.data["firstname"]
    client.lastname = request.data["lastname"]
    client.updated_at = datetime.datetime.utcnow()
    client.save()
    return Response({"Status": "Client general info updated"})


# UPDATE PHONE


@api_view(["PATCH"])
def update_phone(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:

        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        print(client)
    except Client.DoesNotExist:

        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        phone = ClientPhone.objects.get(number=client.phone)
        phone.is_phone_active = False
        client.phone = request.data["phone"]
        client.phone_is_activated = False
        client.updated_at = datetime.datetime.utcnow()
        client.sms_validation_code = request.data["smsCode"]
        newPhone = ClientPhone.objects.create(
            client=client,
            number=request.data["phone"],
            is_phone_active=True,
            created_at=datetime.datetime.utcnow(),
        )
    except db.IntegrityError:

        return Response(
            {"Message": "Ce numéro est déja utilisé"},
            status=status.HTTP_409_CONFLICT,
        )
    client.save()
    phone.save()
    newPhone.save()

    return Response({"Status": "Phone updated"})


# VERIFY SMS CODE CONFIRMATION


@api_view(["POST"])
def verify_phone(request):
    try:
        client = Client.objects.get(phone=request.data["phone"])
    except Client.DoesNotExist:

        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    if client.sms_validation_code == request.data["code"]:
        client.phone_is_activated = True
        client.save()

        return Response({"Status": "Phone verify"})

    return Response({"Error": "Phone not verify"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def is_phone_used(request):
    is_used = True
    try:
        client_phone = ClientPhone.objects.get(number=request.data["phone"])
    except ClientPhone.DoesNotExist:
        is_used = False
    return Response({"used": is_used})


# CREATE ADMIN BACK OFFICE


@api_view(["POST"])
def create_admin(request):
    try:
        token_message = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    if token_message == os.getenv("AUTH"):
        request.data["password"] = make_password(request.data["password"])
        request.data.update({"created_at": datetime.datetime.utcnow()})
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"Status": "Admin created", "Data": serializer.data})
        if serializer.errors.get("username") and serializer.errors.get("email"):

            return Response(
                {"Error": "Email et username déja existant"},
                status=status.HTTP_409_CONFLICT,
            )
        elif serializer.errors.get("username"):

            return Response(
                {"Error": "username déja existant"}, status=status.HTTP_409_CONFLICT
            )
        elif serializer.errors.get("email"):

            return Response(
                {"Error": "email déja existant"}, status=status.HTTP_409_CONFLICT
            )
        else:
            return Response(
                {"Error": "Admin not created"}, status=status.HTTP_404_NOT_FOUND
            )
    return Response({"Error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)


# GET ADMIN
@api_view(["GET"])
def get_admin(request):
    try:
        admin_id = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["admin_id"]
    except jwt.ExpiredSignatureError:

        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        admin = Admin.objects.get(id=admin_id)
    except Admin.DoesNotExist:
        return Response({"Error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(admin.info)


# CREATE REDUCTION CODE


@api_view(["POST"])
@authentication_classes([AdminAuthentication])
def create_reduction_code(request):
    if request.data["code"].strip().__len__() == 0:
        return Response(
            {"Error": "Code must have value"}, status=status.HTTP_400_BAD_REQUEST
        )
    if request.data["reduction"] > 0 and request.data["reduction"] <= 100:
        code = CodeReductionAvailable.objects.create(
            code_name=request.data["code_name"],
            code=request.data["code"],
            reduction=request.data["reduction"],
            client_is_subscribed=True,
            created_at=datetime.datetime.utcnow(),
            expiry_at=request.data["expiry"],
        )
        code.clients.set(request.data["clients"])
        code.subscribes.set(request.data["subscribes"])
        code.save()
        return Response({"Status": "Code created"}, status=status.HTTP_201_CREATED)
    return Response(
        {"Error": "Reduction value must correct"}, status=status.HTTP_400_BAD_REQUEST
    )


# DELETE REDUCTION CODE


@api_view(["DELETE"])
@authentication_classes([AdminAuthentication])
def delete_reduction_code(request, id):
    try:
        code = CodeReductionAvailable.objects.get(id=id)
        code_used = CodeReductionUsed.objects.filter(code_used=code)
    except CodeReductionAvailable.DoesNotExist:
        print("Code not found")
        return Response({"Error": "Code not found"}, status=status.HTTP_404_NOT_FOUND)
    code_used.delete()
    code.delete()
    print(DELETE_SUCCESSFUL)
    return Response({"State": DELETE_SUCCESSFUL})


# UPDATE REDUCTION CODE


@api_view(["PATCH"])
@authentication_classes([AdminAuthentication])
def update_reduction_code(request, id):
    if request.data["code"].strip().__len__() == 0:
        return Response(
            {"Error": "Code  must have value"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if request.data["reduction"] > 0 and request.data["reduction"] <= 100:
        code = CodeReductionAvailable.objects.get(id=id)
        code.code_name = request.data["code_name"]
        code.code = request.data["code"]
        code.expiry_at = request.data["expiry"]
        code.reduction = request.data["reduction"]
        code.updated_at = datetime.datetime.utcnow()
        code.clients.set(request.data["clients"])
        code.subscribes.set(request.data["subscribes"])
        code.save()
        return Response({"State": UPDATE_SUCCESSFUL})
    return Response(
        {"Error": "Reduction value must correct"}, status=status.HTTP_400_BAD_REQUEST
    )


# GET ALL REDUCTION CODE


@authentication_classes([AdminAuthentication])
class ApiReductionCodeListView(ListAPIView):
    queryset = CodeReductionAvailable.objects.all()
    serializer_class = CodeReductionAvailableSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("code",)
    ordering_fields = "__all__"
    pagination_class = ReductionCodePageNumberPagination


# GET ALL CLIENTS WITH ALL INFOS
@authentication_classes([AdminAuthentication])
class ApiSubscriptionListView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("client__firstname", "client__lastname")
    ordering_fields = "__all__"
    pagination_class = ReductionCodePageNumberPagination


# UPDATE CLIENT SUBSCRIBE


@api_view(["PATCH"])
@authentication_classes([AdminAuthentication])
def update_client_subscribe(request, id):
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        subscription = Subscription.objects.get(client=id)
        subscribe = Subscribe.objects.get(id=request.data["subscribe"])
    except (Subscription.DoesNotExist, Subscribe.DoesNotExist) as exception:
        return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    if subscription.subscribe.name != "Freemium" and (
        (
            subscription.subscribe.number_couple_offered == 0
            and subscribe.number_couple_offered != 0
            and subscription.subscribe.number_couple_offered
            < subscribe.number_couple_offered
        )
        or (
            subscription.subscribe.number_couple_offered != 0
            and subscribe.number_couple_offered != 0
            and subscribe.number_couple_offered
            < subscription.subscribe.number_couple_offered
        )
    ):
        client_downgrade = ClientDowngrade.objects.create(
            client=client,
            renew=subscription.end,
            subscribe=subscribe,
            duration=subscription.duration,
        )
        client_downgrade.save()
        print("Downgrade")
    else:
        print("Upgrade")
        subscription.subscribe = subscribe
        subscription.end = request.data["end"]
        subscription.renew_status = request.data["renew"]
        subscription.save()
    return Response({"State": UPDATE_SUCCESSFUL})


####REWARD#####

# GET ALL REWARD
class ApiRewardListView(ListAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = "sum"
    ordering_fields = "__all__"
    pagination_class = RewardPageNumberPagination


# GET REWARD BY ID
@api_view(["GET"])
def get_reward_by_id(request, id):
    try:
        reward = Reward.objects.get(id=id)
    except Reward.DoesNotExist:

        return Response({"Error": REWARD_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    serializer = RewardSerializer(reward, many=False)

    return Response(
        {"Status": "Get subscribe info successfull", "data": serializer.data}
    )


# UPDATE REWARD
@api_view(["PATCH"])
@authentication_classes([AdminAuthentication])
def update_reward(request, id):
    try:
        subscription = Subscription.objects.get(client=id)
    except Subscription.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        reward = Reward.objects.get(id=subscription.client.reward.id)
    except Reward.DoesNotExist:
        print(REWARD_NOT_FOUND)

        return Response({"Error": REWARD_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
    reward.updated_at = datetime.datetime.utcnow()
    reward.sum = request.data["sum"]
    reward.save()
    return Response({"Status": UPDATE_SUCCESSFUL})


####UPDATE FREE DAY###


@api_view(["PATCH"])
@authentication_classes([AdminAuthentication])
def update_reward_free_day(request, id):
    try:
        subscription = Subscription.objects.get(client=id)
    except Subscription.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        reward = Reward.objects.get(id=subscription.client.reward.id)
    except Reward.DoesNotExist:
        print(REWARD_NOT_FOUND)

        return Response({"Error": REWARD_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
    reward.updated_at = datetime.datetime.utcnow()
    reward.free_day = request.data["free_day"]
    reward.save()
    return Response({"Status": UPDATE_SUCCESSFUL})


# GET USER BY TOKEN
@api_view(["GET"])
def get_user_by_token(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    serializer = SubscriptionWithEmailSerializer(subscription, many=False)

    return Response(serializer.data)


# GET USER BY ID
@api_view(["GET"])
@authentication_classes([AdminAuthentication])
def get_user_by_id(request, id):
    try:
        client = Client.objects.get(id=id)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    serializer = SubscriptionWithEmailSerializer(
        subscription, many=False, context={"request": request}
    )

    return Response(serializer.data)


# PAYEMENT
@api_view(["POST"])
def payement(request):
    stripe.api_key = STRIPE_SECRET_KEY
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        reward_client = Reward.objects.get(id=client.reward.id)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        subscription = Subscription.objects.get(client=client)
    except Subscription.DoesNotExist:
        return Response(
            {"Error": "Client non souscrite"}, status=status.HTTP_404_NOT_FOUND
        )
    try:
        subscribe = Subscribe.objects.get(id=request.data["subscribe"])
    except Subscribe.DoesNotExist:
        return Response(
            {"Error": "Subcribe not found"}, status=status.HTTP_404_NOT_FOUND
        )
    subscribe_price = subscribe.price - ((subscribe.price * subscribe.reduction) / 100)
    if request.data["duration"] in (30, 365):
        if request.data["duration"] == 365:
            subscribe_price *= 12
        elif request.data["duration"] == 30:
            subscribe_price=subscribe.price
    else:
        return Response({"Error": "Data error"}, status=status.HTTP_400_BAD_REQUEST)
    if (
        request.data["discount_credit"] >= 0
        and request.data["discount_credit"] <= reward_client.sum
        and request.data["discount_code"] >= 0
    ):
        downgrade = True
        try:
            client_downgrade = ClientDowngrade.objects.get(client=client)
        except ClientDowngrade.DoesNotExist:
            downgrade = False
        if downgrade == False:
            prorata = 0
            diff = 0
            if (
                subscription.subscribe.name != "Freemium"
                and subscription.subscribe.id != subscribe.id
                and not (
                    (
                        (
                            subscription.subscribe.number_couple_offered == 0
                            and subscribe.number_couple_offered != 0
                            and subscription.subscribe.number_couple_offered
                            < subscribe.number_couple_offered
                        )
                        or (
                            subscription.subscribe.number_couple_offered != 0
                            and subscribe.number_couple_offered != 0
                            and subscribe.number_couple_offered
                            < subscription.subscribe.number_couple_offered
                        )
                    )
                )
            ):
                old_price = subscription.subscribe.price - (
                    (subscription.subscribe.price * subscription.subscribe.reduction)
                    / 100
                )
                start = datetime.datetime.utcnow()
                end = subscription.end.replace(tzinfo=None)
                price_per_day = 0
                days = []
                index = 0
                days.append([])
                for x in arrow.Arrow.range("day", start, end):
                    if x.day == 1:
                        days.append([])
                        index += 1
                    days[index].append(x.day)
                for i, day in enumerate(days):
                    if i < days.__len__() - 1:
                        price_per_day = old_price / day[len(day) - 1]
                    else:
                        price_per_day = old_price / monthrange(end.year, end.month)[1]
                    prorata += price_per_day * len(day)

                prorata = float("{:.2f}".format(prorata))
                price = subscribe.price - (
                    (subscribe.price * subscribe.reduction) / 100
                )
                if subscription.duration == 365:
                    price *= 12
                if prorata > price:
                    diff += prorata - price
                    prorata = price

            customer = stripe.Customer.create(
                name=request.data["author"],
            )
            try:
                paymentResult = stripe.PaymentIntent.create(
                    amount=format_amount(
                        subscribe_price
                        - prorata
                        - request.data["discount_credit"]
                        - request.data["discount_code"]
                    ),
                    currency="eur",
                    payment_method_types=["card"],
                    payment_method_data={
                        "type": "card",
                        "card[token]": request.data["card_token"],
                    },
                    customer=customer,
                    confirm=True,
                    receipt_email=client.email,
                    setup_future_usage="on_session",
                )
            except Exception as e:
                print(" 💥 💥 Error inside Exception = {}".format(e))
                return Response(
                    {"Error": "Erreur de carte"}, status=status.HTTP_404_NOT_FOUND
                )

            client.customers_id = customer.id
            client.save()
            date = datetime.datetime.utcnow()
            try:
                    reduction_code=CodeReductionAvailable.objects.get(code = request.data['code'])
            except CodeReductionAvailable.DoesNotExist:
                    return Response(
                {"Error": "Code not found"}, status=status.HTTP_400_BAD_REQUEST
            )    
            reduction_code_used = CodeReductionUsed.objects.create(
                    code_used=reduction_code,
                    client=client,
                    code=reduction_code.code,
                    used_date=date,
                    created_at=date,
                )
            reduction_code_used.save()
            if subscription.subscribe.name != "Freemium" and (
                (
                    subscription.subscribe.number_couple_offered == 0
                    and subscribe.number_couple_offered != 0
                    and subscription.subscribe.number_couple_offered
                    < subscribe.number_couple_offered
                )
                or (
                    subscription.subscribe.number_couple_offered != 0
                    and subscribe.number_couple_offered != 0
                    and subscribe.number_couple_offered
                    < subscription.subscribe.number_couple_offered
                )
            ):
                client_downgrade = ClientDowngrade.objects.create(
                    client=client,
                    renew=subscription.end,
                    subscribe=subscribe,
                    duration=subscription.duration,
                    total_discount=(
                        request.data["discount_credit"] + request.data["discount_code"]
                    ),
                    payment_method_id=paymentResult.payment_method,
                )
                client_downgrade.save()
            else:
                reward = Reward.objects.get(id=client.reward.id)
                reward.total_for_next_subscription += diff
                reward.save()
                subscription.subscribe = subscribe
                subscription.duration = request.data["duration"]
                subscription.start = datetime.datetime.utcnow()
                subscription.end = datetime.datetime.utcnow() + datetime.timedelta(
                    days=request.data["duration"]
                )

                subscription.renew_status = False

                subscription.activate = True

                subscription.payment_method_id = paymentResult.payment_method

                subscription.total_discount = (
                    request.data["discount_credit"] + request.data["discount_code"]
                )
                subscription.updated_at = datetime.datetime.utcnow()
                subscription.save()
            payment = Payment.objects.create(
                subscription=subscription,
                author=request.data["author"],
                created_at=datetime.datetime.utcnow(),
            )
            payment.reference = "PM" + "%06d" % payment.id
            payment.save()
            bill = Invoice.objects.create(
                payment=payment,
                initial_price=subscribe_price,
                discount_credit=request.data["discount_credit"],
                discount_code=request.data["discount_code"],
                nb_crypto_currency=subscribe.number_couple_offered,
                created_at=datetime.datetime.utcnow(),
            )
            bill.final_price = (
                bill.initial_price
                - (bill.discount_credit + bill.discount_code)
                - prorata
            )
            bill.save()
            if reward_client.sum >= request.data["discount_credit"]:
                reward_client.sum -= request.data["discount_credit"]
                reward_client.save()
            if client.relationship_code:
                try:
                    clientReward = SimpleRewardByRelationshipCode.objects.get(
                        client_child_name=client
                    )
                except SimpleRewardByRelationshipCode.DoesNotExist:
                    return Response(
                        {"Error": "Filleul not found"}, status=status.HTTP_404_NOT_FOUND
                    )
                clientReward.reward_credit_by_child = (
                    clientReward.reward_credit_by_child
                    + get_credit_percentage(
                        subscribe_price
                        - prorata
                        - request.data["discount_credit"]
                        - request.data["discount_code"]
                    )
                )
                clientReward.save()
                parrain = Client.objects.get(
                    storage_code_client=client.relationship_code
                )
                parrainReward = Reward.objects.get(id=parrain.reward.id)
                parrainReward.sum = parrainReward.sum + get_credit_percentage(
                    subscribe_price
                    - prorata
                    - request.data["discount_credit"]
                    - request.data["discount_code"]
                )
                parrainReward.save()
                
            return Response({"Status": "Success"})
        else:
            return Response(
                {"Error": "There is downgrade running"}, status=status.HTTP_409_CONFLICT
            )
    return Response(
        {"Error": "There is not enough credit"}, status=status.HTTP_400_BAD_REQUEST
    )


# GET ALL INVOICE
class ApiInvoiceListView(ListAPIView):
    serializer_class = InvoiceSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("payment__reference",)
    ordering_fields = (
        "initial_price",
        "created_at",
        "payment__reference",
        "payment__subscription__subscribe__name",
    )
    pagination_class = InvoicePageNumberPagination

    def get_queryset(self):
        try:
            clientId = jwt.decode(
                get_request_token(self.request),
                os.environ.get("SECRET_KEY"),
                algorithms="HS256",
            )["id"]
        except jwt.ExpiredSignatureError:
            return Response(
                {"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED
            )
        invoice = Invoice.objects.filter(payment__subscription__client__id=clientId)
        return invoice


#### create couple


@api_view(["POST"])
@authentication_classes([AdminAuthentication])
def create_couple(request):
    symbol = request.data["symbol_1"] + request.data["symbol_2"]
    firstInterval = find_first_interval(request.data["intervals"])
    verifySymbol = requests.request(
        "GET",
        f"{os.environ.get('API_BINANCE')}/klines?symbol={symbol}&interval={firstInterval}",
    )
    if "code" in verifySymbol.json():
        return Response(
            {"Error": verifySymbol.json()["msg"]}, status=status.HTTP_404_NOT_FOUND
        )
    try:
        couple = Couple.objects.create(
            symbol_1=request.data["symbol_1"],
            symbol_1_logo=request.data["symbol_1_logo"],
            symbol_2=request.data["symbol_2"],
            symbol_2_logo=request.data["symbol_2_logo"],
            name=request.data["symbol_1"] + "/" + request.data["symbol_2"],
            created_at=datetime.datetime.utcnow(),
            intervals=format_interval(request.data["intervals"]),
        )
    except db.IntegrityError:
        return Response(
            {"status": "Couple already exist"}, status=status.HTTP_409_CONFLICT
        )
    data = encode_multipart_formdata(
        {
            "symbol": symbol,
            "intervals": request.data["intervals"],
        }
    )
    reqUrl = os.environ.get("API_PREDICTION_URL") + "symbol"
    response = requests.request(
        "POST", reqUrl, data=data[0], headers={"Content-Type": data[1]}
    )
    if response.status_code == 200:
        couple.save()
        asset1 = Asset.objects.using("crypto").get(assetname=couple.symbol_1)
        asset2 = Asset.objects.using("crypto").get(assetname=couple.symbol_2)
        return Response(
            {
                "Status": "Couple created",
                "data": response.json(),
                "assetName": asset1.assetfullname + "/" + asset2.assetfullname,
            },
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(
            {"Status": "Couple not created"}, status=status.HTTP_400_BAD_REQUEST
        )


####CREATE COUPLE DEMANDE


@api_view(["POST"])
def create_demande_couple(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    symbol = request.data["symbol"].split("/")
    if symbol.__len__() == 2 and symbol[0].__len__() != 0 and symbol[1].__len__() != 0:
        coupleDemande = CoupleDemand.objects.create(
            created_at=datetime.datetime.utcnow(),
            couple=request.data["symbol"].upper(),
            clients=client,
        )
        coupleDemande.save()
        return Response({"Status": "Demand created"})
    return Response({"Error": "Symbol error"}, status=status.HTTP_400_BAD_REQUEST)


####get all demand
@authentication_classes([AdminAuthentication])
class ApiCoupleDemandeListView(ListAPIView):
    queryset = (
        CoupleDemand.objects.values("couple")
        .annotate(count=Count("couple"))
        .annotate(last_date=Max("created_at"))
    )
    serializer_class = CoupleDemandSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("couple",)
    ordering_fields = ("count", "couple", "last_date")
    pagination_class = CouplePageNumberPagination


###Get all coupl ####


@authentication_classes([AdminAuthentication])
class ApiCoupleListView(ListAPIView):
    queryset = Couple.objects.all()
    serializer_class = CoupleInfoSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name",)
    ordering_fields = "__all__"
    pagination_class = CouplePageNumberPagination


# GET COUPLE BY SYMBOL
@api_view(["GET"])
@authentication_classes([AdminAuthentication])
def get_couple_by_symbol(request, symbol1, symbol2):
    try:
        asset = Couple.objects.get(name=symbol1 + "/" + symbol2)
    except Couple.DoesNotExist:
        return Response({"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    serializer = CoupleInfoSerializer(asset, many=False)
    symbol = asset.name.split("/")
    try:
        asset1 = Asset.objects.using("crypto").get(assetname=symbol[0])
    except Asset.DoesNotExist:
        return Response({"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        asset2 = Asset.objects.using("crypto").get(assetname=symbol[1])
    except Asset.DoesNotExist:
        return Response({"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    data = serializer.data
    data["symbol_1_logo"] = request.build_absolute_uri("/") + data["symbol_1_logo"][1:]
    data["symbol_2_logo"] = request.build_absolute_uri("/") + data["symbol_2_logo"][1:]
    data["intervals"] = sort_interval(data["intervals"])
    data["assetFullName"] = asset1.assetfullname + "/" + asset2.assetfullname
    h24 = 0
    if CoupleData.objects.filter(couple__name=data["name"]).count() != 0:
        end = datetime.datetime.today()
        start = end - datetime.timedelta(hours=24)
        coupleData = CoupleData.objects.filter(
            couple__name=data["name"], enddatetime__range=[start, end]
        )
        dataStart = coupleData.first()
        dataEnd = coupleData.last()
        if dataEnd != None and dataStart != None:
            h24 = ((dataEnd.close - dataStart.close) * 100) / dataStart.close
    data["h24"] = format_h24(h24)
    ################### GET TRAINING ##########

    symbolTrain = asset.name.replace("/", "")
    training = Training.objects.using("crypto").filter(symbolid__symbol=symbolTrain)
    intervalTimes = (
        Training.objects.using("crypto")
        .filter(symbolid__symbol=symbolTrain)
        .values("intervaltime")
        .annotate(dcount=Count("intervaltime"))
    )
    result = []
    index = 0
    for interval in intervalTimes:
        result.append({})
        train = training.filter(intervaltime=interval["intervaltime"])
        result[index]["status"] = get_training_state(
            train[0].trainingstate, train[1].trainingstate, train[2].trainingstate
        )
        result[index]["precision"] = get_precision(
            symbolTrain, interval["intervaltime"]
        )
        result[index]["interval"] = interval["intervaltime"]
        index += 1
    return Response(
        {
            "Status": "Get Couple info successfull",
            "data": data,
            "precision_data": result,
        }
    )

# GET COUPLE BY SYMBOL FRONT-OFFICE    
@api_view(["GET"])
def get_couple_user(request, symbol1, symbol2):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response(
            {"Error": TOKEN_EXPIRED},
            status=rest_framework.status.HTTP_401_UNAUTHORIZED,
        )
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response(
            {"Error": CLIENT_NOT_FOUND},
            status=rest_framework.status.HTTP_404_NOT_FOUND,
        )
    try:
        coupleFavorite = CoupleFavorite.objects.filter(client=client)
    except CoupleFavorite.DoesNotExist:
        return Response(
            {"Error": FAVORITE_NOT_FOUND},
            status=rest_framework.status.HTTP_404_NOT_FOUND,
        )
    try:
        asset = Couple.objects.get(name=symbol1 + "/" + symbol2)
    except Couple.DoesNotExist:
        return Response({"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    serializer = CoupleInfoSerializer(asset, many=False)
    symbol = asset.name.split("/")
    try:
        asset1 = Asset.objects.using("crypto").get(assetname=symbol[0])
    except Asset.DoesNotExist:
        return Response({"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        asset2 = Asset.objects.using("crypto").get(assetname=symbol[1])
    except Asset.DoesNotExist:
        return Response({"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    data = serializer.data
    data["symbol_1_logo"] = request.build_absolute_uri("/") + data["symbol_1_logo"][1:]
    data["symbol_2_logo"] = request.build_absolute_uri("/") + data["symbol_2_logo"][1:]
    data["intervals"] = sort_interval(data["intervals"])
    data["assetFullName"] = asset1.assetfullname + "/" + asset2.assetfullname
    h24 = 0
    if CoupleData.objects.filter(couple__name=data["name"]).count() != 0:
        end = datetime.datetime.today()
        start = end - datetime.timedelta(hours=24)
        coupleData = CoupleData.objects.filter(
            couple__name=data["name"], enddatetime__range=[start, end]
        )
        dataStart = coupleData.first()
        dataEnd = coupleData.last()
        h24 = ((dataEnd.close - dataStart.close) * 100) / dataStart.close
    data["h24"] = format_h24(h24)
    favorite=False
    for coupleFav in coupleFavorite:
        if coupleFav.couple.name==data["name"]:
            favorite=True
    data["favorite"]=favorite
    return Response(
        {
            "Status": "Get Couple info successfull",
            "data": data,
        }
    )

###DELETE COUPLE #####


@api_view(["DELETE"])
@authentication_classes([AdminAuthentication])
def delete_couple(request, id):

    try:
        couple = Couple.objects.get(id=id)
        couple.delete()
    except Couple.DoesNotExist:
        print("Coupe not found")

        return Response({"Error": COUPLE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

    print(DELETE_SUCCESSFUL)
    return Response({"State": DELETE_SUCCESSFUL})


###Update Coupl Status###


@api_view(["PUT"])
def update_couple_status(request, id):
    try:
        asset = Couple.objects.get(id=id)
    except Couple.DoesNotExist:
        print(COUPLE_NOT_FOUND)
        return Response({"Error": COUPLE_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
    asset.status = request.data["status"]
    asset.save()
    print("Update Couple success")

    return Response({"Status": "Update success"})


###UPDATE COUPLE SYMBOL INFO ####


@api_view(["PATCH"])
@authentication_classes([AdminAuthentication])
def update_couple_info(request, id):
    try:
        couple = Couple.objects.get(id=id)
    except Couple.DoesNotExist:
        return Response({"Error": "Symbol Not found"}, status=status.HTTP_404_NOT_FOUND)
    symbol = request.data["symbol_1"] + request.data["symbol_2"]
    firstInterval = find_first_interval(request.data["intervals"])
    verifySymbol = requests.request(
        "GET",
        f"{os.environ.get('API_BINANCE')}/klines?symbol={symbol}&interval={firstInterval}",
    )
    if "code" in verifySymbol.json():
        return Response(
            {"Error": verifySymbol.json()["msg"]}, status=status.HTTP_404_NOT_FOUND
        )
    if request.data["symbol_1_logo"] != "undefined":
        couple.symbol_1_logo = request.data["symbol_1_logo"]
    if request.data["symbol_2_logo"] != "undefined":
        couple.symbol_2_logo = request.data["symbol_2_logo"]
    couple.symbol_1 = request.data["symbol_1"]
    couple.symbol_2 = request.data["symbol_2"]
    couple.name = request.data["symbol_1"] + "/" + request.data["symbol_2"]
    couple.updated_at = datetime.datetime.utcnow()
    couple.intervals = format_interval(request.data["intervals"])
    data = encode_multipart_formdata(
        {
            "symbol": symbol,
            "intervals": request.data["intervals"],
        }
    )
    reqUrl = os.environ.get("API_PREDICTION_URL") + "symbol"
    response = requests.request(
        "POST", reqUrl, data=data[0], headers={"Content-Type": data[1]}
    )
    if response.status_code == 200:
        try:
            couple.save()
        except db.IntegrityError:
            return Response(
                {"status": "Couple already exist"}, status=status.HTTP_409_CONFLICT
            )
        try:
            asset1 = Asset.objects.using("crypto").get(assetname=couple.symbol_1)
        except Asset.DoesNotExist:
            return Response(
                {"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            asset2 = Asset.objects.using("crypto").get(assetname=couple.symbol_2)
        except Asset.DoesNotExist:
            return Response(
                {"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {
                "Status": "Update Info Couple success",
                "data": asset1.assetfullname + "/" + asset2.assetfullname,
            }
        )
    else:
        return Response(
            {"Status": "Couple not created"}, status=status.HTTP_400_BAD_REQUEST
        )


###CHANGE AUTHORIZED STATUS OF PAIRE######


@api_view(["PATCH"])
def change_validated_status(request, id):

    try:
        couple = Couple.objects.get(id=id)
    except Couple.DoesNotExist:

        return Response({"Error": COUPLE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

    couple.is_authorised = True

    couple.save()
    return Response({"Status": "Change Authorised successfull"})


####CREATE FAVORITE COUPLE


@api_view(["POST"])
def create_favorite_couple(request):
    couple_name = request.data["couple"].split("/")
    if (
        couple_name.__len__() == 2
        and couple_name[0].__len__() != 0
        and couple_name[1].__len__() != 0
        and couple_name[0].isupper()
        and couple_name[1].isupper()
    ):
        try:
            clientId = jwt.decode(
                get_request_token(request),
                os.environ.get("SECRET_KEY"),
                algorithms="HS256",
            )["id"]
        except jwt.ExpiredSignatureError:
            return Response(
                {"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED
            )
        try:
            client = Client.objects.get(id=clientId)
        except Client.DoesNotExist:
            return Response(
                {"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            couple = Couple.objects.get(name=request.data["couple"])
        except Couple.DoesNotExist:
            return Response(
                {"Error": COUPLE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )
        request.data.update(
            {
                "client": client.id,
                "couple": couple.id,
                "created_at": datetime.datetime.utcnow(),
            }
        )
        try:
            CoupleFavorite.objects.get(client=client, couple=couple)
        except CoupleFavorite.DoesNotExist:
            coupleFavorite = CoupleFavoriteSerializer(data=request.data)
            if coupleFavorite.is_valid():
                coupleFavorite.save()
                return Response({"Status": "Favorite couple created"})
            return Response(
                {"Error": "Favorite couple not created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"Error": "Favorite couple already exist"}, status=status.HTTP_409_CONFLICT
        )
    return Response(
        {"Error": "Couple error"},
        status=status.HTTP_400_BAD_REQUEST,
    )


####DELETE FAVORITE COUPLE ####


@api_view(["DELETE"])
def delete_favorite_couple(request, symbol1, symbol2):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        couple = Couple.objects.get(name=symbol1 + "/" + symbol2)
    except Couple.DoesNotExist:
        return Response({"Error": COUPLE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

    try:
        coupleFavorite = CoupleFavorite.objects.get(client=client, couple=couple)
    except CoupleFavorite.DoesNotExist:
        return Response({"Error": FAVORITE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    coupleFavorite.delete()
    return Response({"State": "Favorite couple deleted "})


# CREATE TICKET


@api_view(["POST"])
def create_ticket(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    request.data.update({"created_at": datetime.datetime.utcnow(), "client": client.id})
    data_ticket = {
        "client": request.data["client"],
        "name": request.data["name"],
        "created_at": request.data["created_at"],
    }
    ticket = CreateTicketSerializer(data=data_ticket)
    if ticket.is_valid():
        ticket.save()
        data_message = {
            "ticket": ticket.data["id"],
            "author": client.firstname + " " + client.lastname,
            "message": request.data["message"],
            "date_message": request.data["created_at"],
            "created_at": request.data["created_at"],
            "is_admin": False,
        }
        ticketMessage = CreateTicketMessageSerializer(data=data_message)
        if ticketMessage.is_valid():
            ticketMessage.save()
            return Response({"Status": "Ticket created"})
    return Response({"Error": ticket.errors}, status=status.HTTP_400_BAD_REQUEST)


# GET ALL TICKETS
@authentication_classes([AdminAuthentication])
class ApiTicketListView(ListAPIView):
    serializer_class = TicketSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name", "client__firstname")
    ordering_fields = "__all__"
    pagination_class = InvoicePageNumberPagination

    def get_queryset(self):
        params = self.request.query_params.get("show_all")
        if params and params == "true":
            return Ticket.objects.all()
        else:
            return Ticket.objects.exclude(status=False)


# GET CLIENT TIKECT
class ApiClientTicketListView(ListAPIView):
    serializer_class = TicketSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name",)
    ordering_fields = "__all__"
    pagination_class = InvoicePageNumberPagination

    def get_queryset(self):
        try:
            clientId = jwt.decode(
                get_request_token(self.request),
                os.environ.get("SECRET_KEY"),
                algorithms="HS256",
            )["id"]
        except jwt.ExpiredSignatureError:
            return Response(
                {"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED
            )
        ticket = Ticket.objects.filter(client__id=clientId)
        return ticket


# GET TICKET DETAILS
@api_view(["GET"])
def ticket_details(request, id):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        ticket = Ticket.objects.get(id=id, client=client)
    except Ticket.DoesNotExist:
        return Response({"Error": TICKET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    ticketData = TicketSerializer(ticket, many=False)
    ticketMessage = TicketMessage.objects.filter(ticket=ticket.id)
    messages = TicketMessageSerializer(ticketMessage, many=True)
    return Response({"ticket": ticketData.data, "messages": messages.data})


# GET TICKET DETAILS FOR ADMIN
@api_view(["GET"])
@authentication_classes([AdminAuthentication])
def admin_ticket_details(request, id):
    try:
        adminId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["admin_id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        admin = Admin.objects.get(id=adminId)
    except Admin.DoesNotExist:
        return Response({"Error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return Response({"Error": TICKET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    ticketData = TicketSerializer(ticket, many=False)
    ticketMessage = TicketMessage.objects.filter(ticket=ticket.id)
    messages = TicketMessageSerializer(ticketMessage, many=True)
    profil = request.build_absolute_uri("/") + "images/" + str(ticket.client.profil)
    return Response(
        {"ticket": ticketData.data, "messages": messages.data, "profil": profil}
    )


# UPDATE TICKET STATUS
@api_view(["PATCH"])
def update_ticket_status(request, id):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        ticket = Ticket.objects.get(id=id, client=client)
    except Ticket.DoesNotExist:
        return Response({"Error": TICKET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    ticket.status = request.data["status"]
    ticket.updated_at = datetime.datetime.utcnow()
    ticket.save()
    return Response({"Status": "Ticket status updated"})


# UPDATE TICKET STATUS ADMIN
@api_view(["PATCH"])
@authentication_classes([AdminAuthentication])
def update_admin_ticket_status(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return Response({"Error": TICKET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    ticket.status = request.data["status"]
    ticket.updated_at = datetime.datetime.utcnow()
    ticket.save()
    return Response({"Status": "Ticket status updated"})


# CREATE TICKET MESSAGE
@api_view(["POST"])
def create_ticket_message(request, id):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        ticket = Ticket.objects.get(id=id, client=client)
    except Ticket.DoesNotExist:
        return Response({"Error": TICKET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    message = request.data["message"]
    if message.strip().__len__() == 0:
        return Response(
            {"Error": "There is no message"}, status=status.HTTP_400_BAD_REQUEST
        )
    request.data.update(
        {
            "created_at": datetime.datetime.utcnow(),
            "date_message": datetime.datetime.utcnow(),
            "ticket": ticket.id,
            "is_admin": False,
        }
    )
    message = CreateTicketMessageSerializer(data=request.data)
    if message.is_valid():
        message.save()
        return Response({"Status": "Ticket created"})
    return Response({"Error": message.errors}, status=status.HTTP_400_BAD_REQUEST)


# CREATE TICKET MESSAGE FOR ADMIN
@api_view(["POST"])
@authentication_classes([AdminAuthentication])
def create_admin_ticket_message(request, id):
    try:
        adminId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["admin_id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        admin = Admin.objects.get(id=adminId)
    except Admin.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return Response({"Error": TICKET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    message = request.data["message"]
    if message.strip().__len__() == 0:
        return Response(
            {"Error": "There is no message"}, status=status.HTTP_400_BAD_REQUEST
        )
    request.data.update(
        {
            "created_at": datetime.datetime.utcnow(),
            "date_message": datetime.datetime.utcnow(),
            "ticket": ticket.id,
            "is_admin": True,
        }
    )
    message = CreateTicketMessageSerializer(data=request.data)
    if message.is_valid():
        message.save()
        return Response({"Status": "Ticket created"})
    return Response({"Error": message.errors}, status=status.HTTP_400_BAD_REQUEST)


# GET CLIENT FILLEUL
class ApiClientFilleulListView(ListAPIView):
    serializer_class = ClientRewardSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    ordering_fields = (
        "client_child_name",
        "reward_day_by_child",
        "reward_credit_by_child",
    )
    pagination_class = InvoicePageNumberPagination

    def get_queryset(self):
        code = self.request.get_full_path().split("/")[3].split("?")[0]
        client = SimpleRewardByRelationshipCode.objects.filter(
            client_child_name__relationship_code=code
        )
        return client


# VERIFY PARRAINAGE CODE
@api_view(["POST"])
@authentication_classes([])
def verify_sponsor_code(request):
    try:
        client = Client.objects.get(storage_code_client=request.data["code"])
    except Client.DoesNotExist:
        return Response({"Status": False})
    return Response({"Status": True})


# GET ALL COUPLE
@api_view(["GET"])
def get_all_couple(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response(
            {"Error": TOKEN_EXPIRED},
            status=rest_framework.status.HTTP_401_UNAUTHORIZED,
        )
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response(
            {"Error": CLIENT_NOT_FOUND},
            status=rest_framework.status.HTTP_404_NOT_FOUND,
        )
    try:
        coupleFavorite = CoupleFavorite.objects.filter(client=client)
    except CoupleFavorite.DoesNotExist:
        return Response(
            {"Error": FAVORITE_NOT_FOUND},
            status=rest_framework.status.HTTP_404_NOT_FOUND,
        )
    ordering = ""
    search = ""
    if "search" in request.query_params:
        search = request.query_params["search"]
        couples = Couple.objects.filter(name__icontains=search).exclude(status=0)
    else:
        couples = Couple.objects.all().exclude(status=0)
    if (
        "ordering" in request.query_params
        and "name" in request.query_params["ordering"]
    ):
        couples = couples.order_by(request.query_params["ordering"])
    elif "ordering" in request.query_params:
        ordering = request.query_params["ordering"]
    clientFavorite = []
    ownCouples = []
    finalResult = []
    clientCouples = subscription.couples.all()
    allCouples = []
    couplesName = Couple.objects.values_list("name")

    # GET ALL COUPLE DEMAND
    coupleDemand = CoupleDemand.objects.values_list("couple")
    allCoupleDemand = [item[0] for item in coupleDemand]
    # GET ALL COUPLE NAME

    for coupleName in couplesName:
        allCouples.append(coupleName[0])

    # GET ALL SYMBOL NAME

    symbolName = []
    symbols = (
        Symbol.objects.using("crypto")
        .exclude(usable=0)
        .values_list("baseasset__assetname", "quoteasset__assetname")
    )
    for symbol in symbols:
        symbolName.append("/".join(symbol))

    # GET DIFFERENCE OF COUPLE AND SYMBOL

    for item in symbolName:
        if item not in allCouples:
            status = False
            if item in allCoupleDemand:
                status = True
            if item.__contains__(search):
                finalResult.append(
                    {
                        "symbol": item,
                        "openStart": 0,
                        "openNow": 0,
                        "closeStart": 0,
                        "closeNow": 0,
                        "lowStart": 0,
                        "lowNow": 0,
                        "highStart": 0,
                        "highNow": 0,
                        "h24": 0,
                        "volume": 0,
                        "favorite": False,
                        "status": "requested" if status == True else "unrequested",
                        "coupleId": 0,
                        "assetFullName": "",
                    }
                )
    for ownCouple in clientCouples:
        ownCouples.append(ownCouple.name)
    for coupleFav in coupleFavorite:
        clientFavorite.append(coupleFav.couple.name)
    for couple in couples:
        end = datetime.datetime.today()
        start = end - datetime.timedelta(hours=24)
        try:
            asset1 = Asset.objects.using("crypto").get(assetname=couple.symbol_1)
        except Asset.DoesNotExist:
            return Response(
                {"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            asset2 = Asset.objects.using("crypto").get(assetname=couple.symbol_2)
        except Asset.DoesNotExist:
            return Response(
                {"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )
        asset = asset1.assetfullname + "/" + asset2.assetfullname
        favorite = False
        state = False
        if couple.name in clientFavorite:
            favorite = True
        if couple.name in ownCouples:
            state = True
        coupleData = CoupleData.objects.filter(
            couple=couple, enddatetime__range=[start, end]
        )
        max_high = 0
        max_low = 0
        max_close = 0
        try:
            cnx = mysql.connector.connect(**dbConfig)
            cursor = cnx.cursor(buffered=True)
            end_date = datetime.datetime.today()
            start_date = end - datetime.timedelta(hours=24)
            query = f"""select tag,prediction from prediction_data_{couple.name.replace('/','')} where datetime between %s and %s"""
            cursor.execute(query, (start_date, end_date))
            for (tag, prediction) in cursor:
                if tag == "high":
                    if max_high == 0 or prediction > max_high:
                        max_high = prediction
                if tag == "low":
                    if max_low == 0 or prediction > max_low:
                        max_low = prediction
                if tag == "close":
                    if max_close == 0 or prediction > max_close:
                        max_close = prediction
        except mysql.connector.Error as err:
            cursor.close()
            cnx.close()

        if coupleData.count() > 0:
            dataStart = dict2obj(
                {
                    "high": (coupleData.aggregate(Max("high")).get("high__max")),
                    "low": (coupleData.aggregate(Max("low")).get("low__max")),
                    "close": (coupleData.aggregate(Max("close")).get("close__max")),
                    "open": (coupleData.aggregate(Max("open")).get("open__max")),
                    "volume": (coupleData.aggregate(Max("volume")).get("volume__max")),
                }
            )
            dataEnd = dict2obj(
                {
                    "high": max_high,
                    "low": max_low,
                    "close": max_close,
                    "open": coupleData.last().open,
                    "volume": coupleData.last().volume,
                }
            )
            h24 = ((dataEnd.close - dataStart.close) * 100) / dataStart.close
        else:
            dataStart = dict2obj(
                {
                    "high": 0,
                    "low": 0,
                    "close": 0,
                    "open": 0,
                    "volume": 0,
                }
            )
            dataEnd = dataStart
            h24 = 0

        if couple.name.__contains__(search):
            finalResult.append(
                {
                    "symbol": couple.name,
                    "openStart": round(dataStart.open, 2),
                    "openNow": round(dataEnd.open, 2),
                    "closeStart": round(dataStart.close, 2),
                    "closeNow": round(dataEnd.close, 2),
                    "lowStart": round(dataStart.low, 2),
                    "lowNow": round(dataEnd.low, 2),
                    "highStart": round(dataStart.high, 2),
                    "highNow": round(dataEnd.high, 2),
                    "h24": format_h24(h24),
                    "volume": round(dataEnd.volume, 2)
                    if couple.name.find("/USDT")
                    else 0,
                    "favorite": favorite,
                    "status": "owned" if state == True else "unowned",
                    "coupleId": couple.id,
                    "assetFullName": asset,
                }
            )
    finalResult.reverse()
    if ordering in (
        "symbol",
        "-symbol",
        "openStart",
        "-openStart",
        "closeStart",
        "-closeStart",
        "lowStart",
        "-lowStart",
        "highStart",
        "-highStart",
        "h24",
        "-h24",
        "volume",
        "-volume",
    ):
        if ordering.find("-") == -1:
            finalResult.sort(
                key=lambda k: k[ordering.replace("-", "")],
                reverse=False,
            )
        else:
            finalResult.sort(
                key=lambda k: k[ordering.replace("-", "")],
                reverse=True,
            )
    size = 0
    page = 0
    if "size" in request.query_params:
        size = request.query_params["size"]
    if "page" in request.query_params:
        page = request.query_params["page"]
    paginator = None
    next_page = None
    previous_page = None
    if int(size) > 0:
        paginator = Paginator(finalResult, size)
    if int(page) > 0 and int(page) <= paginator.num_pages:
        finalResult = paginator.page(page).object_list
        has_next = paginator.page(page).has_next()
        has_prev = paginator.page(page).has_previous()
    if has_next:
        next_page = replaceTextBetween(
            request.build_absolute_uri(), "page=", "&", str(int(page) + 1)
        )
    if has_prev:
        previous_page = replaceTextBetween(
            request.build_absolute_uri(), "page=", "&", str(int(page) - 1)
        )
    return Response(
        {
            "count": paginator.count,
            "next": next_page,
            "previous": previous_page,
            "results": finalResult,
        }
    )


# GET COUPLE DATA
@api_view(["GET"])
def get_couple_data(request, symbol):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        subscription = Subscription.objects.get(client=client)
        couples = subscription.couples.all()
    except Subscription.DoesNotExist:
        return Response(
            {"Error": "Client non souscrite"}, status=status.HTTP_404_NOT_FOUND
        )
    if "interval" in request.query_params:
        interval = request.query_params["interval"]
    else:
        return Response({"Error": "Pas d'interval"}, status=status.HTTP_400_BAD_REQUEST)
    dataResult = []
    date_now = datetime.datetime.utcnow()
    endtimestamp = to_timestamp_milliseconds(round_minutes(date_now,interval))

    # parametrage type interval j/h/m
    if interval[-1] == 'm' :
        tmp_limit = PARM_INTERVAL['minute']
        add_time=int(interval[0:-1])*60*1000
    elif interval[-1] == 'h' :
        tmp_limit = PARM_INTERVAL['hour']
        add_time=int(interval[0:-1])*3600*1000
    else:
        tmp_limit = PARM_INTERVAL['day']
        add_time=int(interval[0:-1])*24*3600*1000
    limit = int(tmp_limit) * int(interval[0:-1])
    try:
        cnx = mysql.connector.connect(**dbConfig)
        cursor = cnx.cursor(buffered=True)
        filter= make_filter_interval(interval,2)
        query = f"""select high,low,close,open,intervaltime,endtimestamp,volume from main_data_{symbol} where intervaltime='1{interval[-1]}'and endtimestamp <= {endtimestamp} order by enddatetime desc limit {limit}"""
        cursor.execute(query)
        first_item = True
        tmp = 0
        tmp_data = {
            "endtimestamp": False,
            "open": False,
            "high": False,
            "low": False,
            "close": False,
            "volume": False
        }
        for (high, low, close, open, intervaltime, endtimestamp, volume) in cursor:
            if interval[-1] == 'm':
                if first_item:
                    first_item = False
                else:
                    diff = math.ceil((tmp - endtimestamp) / 60000)
                    # Tester si l'écart entre le temps précédent et temps courant dépasse d'une minute
                    if diff != 1:
                        tmp_time = tmp_data['endtimestamp']
                        for x in range(1, diff):
                            tmp_time -= 60000
                            dataResult.append([tmp_time + 1, tmp_data['open'], tmp_data['high'], tmp_data['low'], tmp_data['close'], tmp_data['volume']])

                tmp = endtimestamp

                tmp_data['endtimestamp'] = endtimestamp
                tmp_data['open'] = open
                tmp_data['high'] = high
                tmp_data['low'] = low
                tmp_data['close'] = close
                tmp_data['volume'] = volume

            dataResult.append([endtimestamp + 1-add_time, open, high, low, close, volume])

    except mysql.connector.Error as err:
        cursor.close()
        cnx.close()
        return Response(
            {"Error": ERROR_DB_CONNECT.format(err)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    cursor.close()
    cnx.close()
    if int(interval[0:-1]) == 1 :
        data=dataResult[::-1]
    else:
        j=0
        data=[]
        while j < limit:
            data.append(dataResult[j:j+int(interval[0:-1])])
            j+=int(interval[0:-1])
        dataResponse=[]
        for i in range(0,data.__len__()):
            temp = []
            highData = []
            lowData = []
            bloc = []
            sum = 0
            bloc = data[i]
            temp.append(substract_time(interval,bloc[0][0]))
            temp.append(bloc[bloc.__len__()- 1][1])
            for k in range(0,bloc.__len__()):
              highData.append(bloc[k][2])
            maximum=max(highData)
            temp.append(maximum)
            for k in range(0,bloc.__len__()):
             lowData.append(bloc[k][3])
            minimum=min(lowData)
            temp.append(minimum) 
            for k in range(0,bloc.__len__()):
             sum = sum + bloc[k][5]
            temp.append(bloc[0][4])
            temp.append(sum)
            dataResponse.append(temp)
        data=dataResponse[::-1]
    return Response({"data": data})

# GET COUPLE PREDICTION
@api_view(["GET"])
def get_couple_prediction(request, symbol):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        subscription = Subscription.objects.get(client=client)
        couples = subscription.couples.all()
    except Subscription.DoesNotExist:
        return Response(
            {"Error": "Client non souscrite"}, status=status.HTTP_404_NOT_FOUND
        )
    authorized = False
    for item in couples:
        if item.name.replace("/", "") == symbol:
            authorized = True
    if "interval" in request.query_params:
        interval = request.query_params["interval"]
    else:
        return Response({"Error": "Pas d'interval"}, status=status.HTTP_400_BAD_REQUEST)
    predictionResult = []
    filter= make_filter_interval(interval,500)
    if authorized:
        try:
            cnx = mysql.connector.connect(**dbConfig)
            cursor = cnx.cursor(buffered=True)
            query = f"""select predictime,tag,prediction,intervaltime from prediction_data_{symbol} where intervaltime='{interval}' and predictime in {filter} order by datetime desc"""
            cursor.execute(query)
            for (predictime, tag, prediction, intervaltime) in cursor:
                predictionResult.append(
                    {
                        "predictime": predictime,
                        "tag": tag,
                        "prediction": prediction,
                        "interval": intervaltime,
                    }
                )
        except mysql.connector.Error as err:
            cursor.close()
            cnx.close()
            return Response(
                {"Error": ERROR_DB_CONNECT.format(err)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        cursor.close()
        cnx.close()
        return Response({"prediction":predictionResult})
    return Response({"Error":"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)

# GET CLIENT FAVORITE COUPLES
@api_view(["GET"])
def get_client_favorite_couple(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        couple = CoupleFavorite.objects.filter(client=client)
    except CoupleFavorite.DoesNotExist:
        return Response(
            {"Error": "Client favorite couple not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    coupleOwned = [item.name for item in subscription.couples.all()]
    h24 = 0
    serializer = CoupleFavoriteInfoSerializer(couple, many=True)
    data = serializer.data
    for d in data:
        h24 = 0
        owned = True if d["symbol"] in coupleOwned else False
        if CoupleData.objects.filter(couple__name=d["symbol"]).count() != 0:
            end = datetime.datetime.today()
            start = end - datetime.timedelta(hours=24)
            coupleData = CoupleData.objects.filter(
                couple__name=d["symbol"], enddatetime__range=[start, end]
            )
            dataStart = coupleData.first()
            dataEnd = coupleData.last()
            h24 = ((dataEnd.close - dataStart.close) * 100) / dataStart.close
        d["h24"] = format_h24(h24)
        d["symbol_1_logo"] = request.build_absolute_uri("/") + d["symbol_1_logo"][1:]
        d["symbol_2_logo"] = request.build_absolute_uri("/") + d["symbol_2_logo"][1:]
        d["owned"] = owned
        d["favorite"] = True
    return Response({"data": data})


# ADD DAYS TO SUBSCRIPTION
@api_view(["POST"])
def add_days_to_subscription(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        reward = Reward.objects.get(id=client.reward.id)
    except Reward.DoesNotExist:
        return Response({"Error": REWARD_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        subscription = Subscription.objects.get(client=client)
    except Subscription.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    if request.data["days"] > 0 and request.data["days"] <= reward.free_day:
        subscription.end = subscription.end + datetime.timedelta(
            days=request.data["days"]
        )
        reward.free_day -= request.data["days"]
        update_date = datetime.datetime.utcnow()
        subscription.updated_at = update_date
        reward.updated_at = update_date
        subscription.save()
        reward.save()
        return Response({"Status": "Add days successfull"})
    return Response({"Error": "Not enough days"}, status=status.HTTP_400_BAD_REQUEST)


# ADD CREDIT FOR NEXT SUBSCRIPTION
@api_view(["POST"])
def add_credit_to_subscription(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        reward = Reward.objects.get(id=client.reward.id)
    except Reward.DoesNotExist:
        return Response({"Error": REWARD_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    if request.data["credits"] > 0 and request.data["credits"] <= reward.sum:
        reward.sum -= request.data["credits"]
        reward.total_for_next_subscription += request.data["credits"]
        reward.updated_at = datetime.datetime.utcnow()
        reward.save()
        return Response({"Status": "Add credits successfull"})
    return Response({"Error": "Not enough credits"}, status=status.HTTP_400_BAD_REQUEST)


# ADD COUPLE FOR VISUALISATION
@api_view(["POST"])
def add_couple_for_visualisation(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    for couple in subscription.couples.all():
        if couple.id not in request.data["couple"]:
            request.data["couple"].append(couple.id)
    if (subscription.subscribe.number_couple_offered == 0) or (
        subscription.couples.all().count()
        < subscription.subscribe.number_couple_offered
    ):
        couple_history = CoupleHistory.objects.create(
            subscription=subscription,
            couple=Couple.objects.get(id=request.data["couple"][0]),
        )
        couple_history.save()
        subscription.couples.set(request.data["couple"])
        subscription.save()
        return Response({"Status": "Add couple for visualisation successfull"})
    else:
        return Response(
            {"Error": "Couple offered excedeed"}, status=status.HTTP_400_BAD_REQUEST
        )


# REMOVE COUPLE FOR VISUALISATION
@api_view(["POST"])
def remove_couple_for_visualisation(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        couple_history = CoupleHistory.objects.get(
            couple__id=request.data["couple"], subscription=subscription
        )
    except CoupleHistory.DoesNotExist:
        return Response({"Error": COUPLE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

    date = couple_history.couple_added + datetime.timedelta(days=REMOVE_COUPLE_WAITING)
    if (
        (datetime.datetime.now().replace(tzinfo=None) > date.replace(tzinfo=None))
    ) and (subscription.couples.all().count() >= 0):
        subscription.couples.remove(request.data["couple"])
        subscription.save()
        couple_history.delete()
        return Response({"Status": "Remove couple for visualisation successfull"})
    else:
        return Response(
            {"Error": "Can't remove couple"}, status=status.HTTP_400_BAD_REQUEST
        )


# VISUALIZE COUPLE (ADD VIEW TO COUPLE)
@api_view(["POST"])
def visualize_couple(request, symbol1, symbol2):
    try:
        couple = Couple.objects.get(name=symbol1 + "/" + symbol2)
    except Couple.DoesNotExist:
        return Response({"Error": ASSET_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    vue = CoupleVue.objects.create(couple=couple)
    couple.vues += 1
    couple.save()
    vue.save()
    return Response({"Status": "Visualize couple successfully"})


# GET MOMENT COUPLE
@api_view(["GET"])
def get_moment_couple(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        coupleFavorite = CoupleFavorite.objects.filter(client=client)
    except CoupleFavorite.DoesNotExist:
        return Response({"Error": FAVORITE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    couples = Couple.objects.all()
    coupleOwned = []
    clientFavorite = []
    result = []
    for couple in subscription.couples.all():
        coupleOwned.append(couple.name)
    for coupleFav in coupleFavorite:
        clientFavorite.append(coupleFav.couple.name)
    for couple in couples:
        asset1 = Asset.objects.using("crypto").get(assetname=couple.symbol_1)
        asset2 = Asset.objects.using("crypto").get(assetname=couple.symbol_2)
        enddate = datetime.datetime.utcnow()
        startdate = enddate - datetime.timedelta(days=VUE_DAYS_INTERVAL)
        vue = CoupleVue.objects.filter(
            couple=couple, date__range=[startdate, enddate]
        ).count()
        if vue > MAX_VUE:
            owned = False
            favorite = False
            if couple.name in coupleOwned:
                owned = True
            if couple.name in clientFavorite:
                favorite = True
            h24 = 0
            end = datetime.datetime.today()
            start = end - datetime.timedelta(hours=24)
            coupleData = CoupleData.objects.filter(
                couple=couple, enddatetime__range=[start, end]
            )
            if coupleData.count() > 0:
                dataStart = coupleData.first()
                dataEnd = coupleData.last()
                h24 = ((dataEnd.close - dataStart.close) * 100) / dataStart.close
            result.append(
                {
                    "id": couple.id,
                    "symbol": couple.name,
                    "fullName": asset1.assetfullname + "/" + asset2.assetfullname,
                    "owned": owned,
                    "symbol_1_logo": request.build_absolute_uri("/")
                    + couple.symbol_1_logo.url[1:],
                    "symbol_2_logo": request.build_absolute_uri("/")
                    + couple.symbol_2_logo.url[1:],
                    "favorite": favorite,
                    "h24": format_h24(h24),
                }
            )
    return Response({"data": result})


@api_view(["GET"])
def get_client_couple(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        coupleFavorite = CoupleFavorite.objects.filter(client=client)
    except CoupleFavorite.DoesNotExist:
        return Response({"Error": FAVORITE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    result = []
    clientFavorite = []
    for coupleFav in coupleFavorite:
        clientFavorite.append(coupleFav.couple.name)
    for couple in subscription.couples.all():
        asset1 = Asset.objects.using("crypto").get(assetname=couple.symbol_1)
        asset2 = Asset.objects.using("crypto").get(assetname=couple.symbol_2)
        favorite = False
        if couple.name in clientFavorite:
            favorite = True
        h24 = 0
        end = datetime.datetime.today()
        start = end - datetime.timedelta(hours=24)
        coupleData = CoupleData.objects.filter(
            couple=couple, enddatetime__range=[start, end]
        )
        if coupleData.count() > 0:
            dataStart = coupleData.first()
            dataEnd = coupleData.last()
            h24 = ((dataEnd.close - dataStart.close) * 100) / dataStart.close
        result.append(
            {
                "id": couple.id,
                "symbol": couple.name,
                "fullName": asset1.assetfullname + "/" + asset2.assetfullname,
                "symbol_1_logo": request.build_absolute_uri("/")
                + couple.symbol_1_logo.url[1:],
                "symbol_2_logo": request.build_absolute_uri("/")
                + couple.symbol_2_logo.url[1:],
                "favorite": favorite,
                "owned": True,
                "h24": format_h24(h24),
            }
        )
    return Response({"data": result})


# LOAD COUPLE DATA
@api_view(["GET"])
def load_couple_data(request):
    couples = Couple.objects.all()
    for couple in couples:
        symbol = couple.name.replace("/", "")
        if CoupleData.objects.filter(couple=couple).count() == 0:
            try:
                cnx = mysql.connector.connect(**dbConfig)
                cursor = cnx.cursor(buffered=True)
                end = datetime.datetime.today()
                start = end - datetime.timedelta(hours=24)
                query = f"""select high,low,close,open,volume,enddatetime,intervaltime from main_data_{symbol} where enddatetime between %s and %s order by enddatetime"""
                cursor.execute(query, (start, end))
                for (
                    high,
                    low,
                    close,
                    open,
                    volume,
                    enddatetime,
                    intervaltime,
                ) in cursor:
                    coupleData = CoupleData.objects.create(
                        couple=couple,
                        enddatetime=enddatetime,
                        high=high,
                        low=low,
                        close=close,
                        open=open,
                        volume=volume,
                        intervaltime=intervaltime,
                    )
                    coupleData.save()
            except mysql.connector.Error as err:
                print(ERROR_DB_CONNECT.format(err))
        else:
            last = str(CoupleData.objects.last().enddatetime).split("+")[0]
            try:
                cnx = mysql.connector.connect(**dbConfig)
                cursor = cnx.cursor(buffered=True)
                query = f"""select high,low,close,open,volume,enddatetime,intervaltime from main_data_{symbol} where enddatetime > %s"""
                cursor.execute(query, (last,))
                for (
                    high,
                    low,
                    close,
                    open,
                    volume,
                    enddatetime,
                    intervaltime,
                ) in cursor:
                    coupleData = CoupleData.objects.create(
                        couple=couple,
                        enddatetime=enddatetime,
                        high=high,
                        low=low,
                        close=close,
                        open=open,
                        volume=volume,
                        intervaltime=intervaltime,
                    )
                    coupleData.save()
            except mysql.connector.Error as err:
                print(ERROR_DB_CONNECT.format(err))

    return Response({"Status": "Load couple data successfull"})


# VALIDATE COUPLE DEMAND
@api_view(["POST"])
@authentication_classes([AdminAuthentication])
def validate_demande(request, symbol1, symbol2):
    coupleDemand = CoupleDemand.objects.filter(couple=symbol1 + "/" + symbol2)
    if coupleDemand.count() == 0:
        return Response(
            {"Error": "Couple demand not found"}, status=status.HTTP_404_NOT_FOUND
        )
    else:
        coupleDemand.delete()
        return Response({"Status": "Couple demand validate"})


# USE REDUCTION CODE
@api_view(["POST"])
def use_reduction_code(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        subscribe = Subscribe.objects.get(id=request.data["subscribe"])
    except Subscribe.DoesNotExist:
        return Response(
            {"Error": "Subcribe not found"}, status=status.HTTP_404_NOT_FOUND
        )
    try:
        reduction_code = CodeReductionAvailable.objects.get(code=request.data["code"])
    except CodeReductionAvailable.DoesNotExist:
        return Response(
            {"Error": "Reduction code not found"}, status=status.HTTP_404_NOT_FOUND
        )
    if (reduction_code.expiry_at.date() - datetime.datetime.now().date()).days < 0:
        return Response({"Error": "Code expired"}, status=status.HTTP_400_BAD_REQUEST)
    clients = reduction_code.clients.all()
    subscribes = reduction_code.subscribes.all()
    if clients.count() > 0:
        if client not in clients:
            return Response(
                {"Error": "Code inapproprié à vous"}, status=status.HTTP_400_BAD_REQUEST
            )
    if subscribes.count() > 0:
        if subscribe not in subscribes:
            return Response(
                {"Error": "Code inapproprié à votre abonnement"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    try:
        CodeReductionUsed.objects.get(client=client, code=request.data["code"])
    except CodeReductionUsed.DoesNotExist:
        return Response({"data": reduction_code.reduction})
    return Response({"Error": "Code used already"}, status=status.HTTP_400_BAD_REQUEST)


# VERIFY TOKEN EXPIRATION
@api_view(["POST"])
def verify_token(request):
    expired = False
    try:
        token = jwt.decode(
            request.data["token"], os.environ.get("SECRET_KEY"), algorithms="HS256"
        )
    except jwt.ExpiredSignatureError:
        expired = True
    return Response({"Expired": expired})


# VERIFY ACCOUNT STATUS
@api_view(["POST"])
def verify_account(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    if client.account_is_active:
        return Response({"status": client.account_is_active})
    else:
        return Response(
            {"Error": "Client account is not active"}, status=status.HTTP_404_NOT_FOUND
        )


# VERIFY PASSWORD
@api_view(["POST"])
def verify_password(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    verify = False
    if check_password(request.data["password"], client.password):
        verify = True
    return Response({"verify": verify})


# GET UPGRADE SUBSCRIBE
class ApiUpgradeSubscribeListView(ListAPIView):
    serializer_class = SubcribeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name",)
    ordering_fields = "__all__"
    pagination_class = SubscribePageNumberPagination

    def get_queryset(self):
        subscribe_id = self.request.get_full_path().split("/")[3].split("?")[0]
        try:
            subscribe = Subscribe.objects.get(id=subscribe_id)
        except Subscribe.DoesNotExist:
            return Subscribe.objects.none()
        return Subscribe.objects.filter(
            number_couple_offered__gt=subscribe.number_couple_offered
        ).exclude(name="Freemium")


# GET LOGS
class ApiLogsList(ListAPIView):
    queryset = APILogsModel.objects.all()
    serializer_class = ApiLogsSeralizer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        "status_code",
        "method",
        "added_on",
    )
    ordering_fields = "__all__"
    pagination_class = LogPageNumberPagination


# GET CLIENT COUPLE BY CLIENT ID
@api_view(["GET"])
@authentication_classes([AdminAuthentication])
def get_couple_client(request, id):
    try:
        client = Client.objects.get(id=id)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        coupleFavorite = CoupleFavorite.objects.filter(client=client)
    except CoupleFavorite.DoesNotExist:
        return Response({"Error": FAVORITE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    result = []
    clientFavorite = []
    for coupleFav in coupleFavorite:
        clientFavorite.append(coupleFav.couple.name)
    for couple in subscription.couples.all():
        asset1 = Asset.objects.using("crypto").get(assetname=couple.symbol_1)
        asset2 = Asset.objects.using("crypto").get(assetname=couple.symbol_2)
        favorite = False
        if couple.name in clientFavorite:
            favorite = True
        h24 = 0
        if CoupleData.objects.filter(couple=couple).count() != 0:
            end = datetime.datetime.today()
            start = end - datetime.timedelta(hours=24)
            coupleData = CoupleData.objects.filter(
                couple=couple, enddatetime__range=[start, end]
            )
            dataStart = coupleData.first()
            dataEnd = coupleData.last()
            if dataStart is not None and dataEnd is not None:
                h24 = ((dataEnd.close - dataStart.close) * 100) / dataStart.close
            else:
                h24 = 0
        result.append(
            {
                "id": couple.id,
                "symbol": couple.name,
                "fullName": asset1.assetfullname + "/" + asset2.assetfullname,
                "symbol_1_logo": request.build_absolute_uri("/")
                + couple.symbol_1_logo.url[1:],
                "symbol_2_logo": request.build_absolute_uri("/")
                + couple.symbol_2_logo.url[1:],
                "favorite": favorite,
                "owned": True,
                "h24": format_h24(h24),
            }
        )
    return Response({"data": result})


# CHECK EXPIRY CLIENT SUBSCRIPTION
@api_view(["POST"])
def check_subscription(request):
    try:
        client = Client.objects.get(id=id)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    if subscription.end.replace(tzinfo=None) <= datetime.datetime.utcnow():
        return Response({"expiry": True})
    return Response({"expiry": False})


# GET EXPLOSIVE COUPLE
@api_view(["GET"])
def get_explosive_couple(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        subscription = Subscription.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        coupleFavorite = CoupleFavorite.objects.filter(client=client)
    except CoupleFavorite.DoesNotExist:
        return Response({"Error": FAVORITE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    couples = Couple.objects.all()
    coupleOwned = []
    clientFavorite = []
    result = []
    for couple in subscription.couples.all():
        coupleOwned.append(couple.name)
    for coupleFav in coupleFavorite:
        clientFavorite.append(coupleFav.couple.name)
    for couple in couples:
        asset1 = Asset.objects.using("crypto").get(assetname=couple.symbol_1)
        asset2 = Asset.objects.using("crypto").get(assetname=couple.symbol_2)
        owned = False
        favorite = False
        if couple.name in coupleOwned:
            owned = True
        if couple.name in clientFavorite:
            favorite = True
        h24 = 0
        end = datetime.datetime.today()
        start = end - datetime.timedelta(hours=24)
        coupleData = CoupleData.objects.filter(
            couple=couple, enddatetime__range=[start, end]
        )
        if coupleData.count() > 0:
            dataStart = coupleData.first()
            dataEnd = coupleData.last()
            h24 = ((dataEnd.close - dataStart.close) * 100) / dataStart.close
            result.append(
                {
                    "id": couple.id,
                    "symbol": couple.name,
                    "fullName": asset1.assetfullname + "/" + asset2.assetfullname,
                    "owned": owned,
                    "symbol_1_logo": request.build_absolute_uri("/")
                    + couple.symbol_1_logo.url[1:],
                    "symbol_2_logo": request.build_absolute_uri("/")
                    + couple.symbol_2_logo.url[1:],
                    "favorite": favorite,
                    "h24": format_h24(h24),
                }
            )
        result.sort(
            key=lambda k: float(k["h24"]),
            reverse=True,
        )
    return Response({"data": result[:6]})


# GET PRORATA VALUE
@api_view(["POST"])
def prorata(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    try:
        subscription = Subscription.objects.get(client=client)
    except Subscription.DoesNotExist:
        return Response(
            {"Error": "Client non souscrite"}, status=status.HTTP_404_NOT_FOUND
        )
    try:
        subscribe = Subscribe.objects.get(id=request.data["subscribe"])
    except Subscribe.DoesNotExist:
        return Response(
            {"Error": "Subcribe not found"}, status=status.HTTP_404_NOT_FOUND
        )
    prorata = 0
    diff = 0
    if (
        subscription.subscribe.name != "Freemium"
        and subscription.subscribe.id != subscribe.id
        and not (
            (
                (
                    subscription.subscribe.number_couple_offered == 0
                    and subscribe.number_couple_offered != 0
                    and subscription.subscribe.number_couple_offered
                    < subscribe.number_couple_offered
                )
                or (
                    subscription.subscribe.number_couple_offered != 0
                    and subscribe.number_couple_offered != 0
                    and subscribe.number_couple_offered
                    < subscription.subscribe.number_couple_offered
                )
            )
        )
    ):
        old_price = subscription.subscribe.price - (
            (subscription.subscribe.price * subscription.subscribe.reduction) / 100
        )
        start = datetime.datetime.utcnow()
        end = subscription.end.replace(tzinfo=None)
        price_per_day = 0
        days = []
        index = 0
        days.append([])
        for x in arrow.Arrow.range("day", start, end):
            if x.day == 1:
                days.append([])
                index += 1
            days[index].append(x.day)
        for i, day in enumerate(days):
            if i < days.__len__() - 1:
                price_per_day = old_price / day[len(day) - 1]
            else:
                price_per_day = old_price / monthrange(end.year, end.month)[1]
            prorata += price_per_day * len(day)

        prorata = float("{:.2f}".format(prorata))
        price = subscribe.price - ((subscribe.price * subscribe.reduction) / 100)
        if subscription.duration == 365:
            price *= 12
        if prorata > price:
            diff += prorata - price
            prorata = price
    return Response({"prorata": prorata, "diff": diff})


# GENERATE AUTH TOKEN
@api_view(["GET"])
@authentication_classes([])
def generateAuthToken(request):
    token = generate_token(os.getenv("AUTH"))["token"]
    return Response({"token": token})


# UPLOAD USER PROFIL
@api_view(["POST"])
def upload_user_profil(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    client.profil = request.data["profil"]
    client.updated_at = datetime.datetime.utcnow()
    client.save()
    return Response({"Status": "Client profil updated"})


# REMOVE COUPLE FOR DOWNGRADE
@api_view(["POST"])
def remove_couple_for_downgrade(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
        client_downgrade = ClientDowngrade.objects.get(client=client)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    client_downgrade.couples.set(request.data["couple"])
    client_downgrade.save()
    return Response({"Status": "Remove couple for downgrade successfull"})


# CHECK DOWNGRADE
@api_view(["POST"])
def check_downgrade(request):
    try:
        clientId = jwt.decode(
            get_request_token(request), os.environ.get("SECRET_KEY"), algorithms="HS256"
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    downgrade = False
    try:
        client_downgrade = ClientDowngrade.objects.get(client=client)
    except ClientDowngrade.DoesNotExist:
        return Response({"status": False})
    try:
        subscription = Subscription.objects.get(client=client)
    except Subscription.DoesNotExist:
        return Response(
            {"Error": "Client non souscrite"}, status=status.HTTP_404_NOT_FOUND
        )
    try:
        subscribe = Subscribe.objects.get(id=client_downgrade.subscribe.id)
    except Subscribe.DoesNotExist:
        return Response(
            {"Error": "Subcribe not found"}, status=status.HTTP_404_NOT_FOUND
        )
    if subscription.couples.all().count() <= subscribe.number_couple_offered:
        return Response({"status": False})
    if client_downgrade.couples.count() == 0:
        downgrade = True
    return Response({"status": downgrade, "subscribe": client_downgrade.subscribe.id})


# UPDATE SUBSCRIPTION RENEW STATUS
@api_view(["PATCH"])
def renew_subscription_status(request):
    if "renew" in request.data:
        try:
            clientId = jwt.decode(
                get_request_token(request),
                os.environ.get("SECRET_KEY"),
                algorithms="HS256",
            )["id"]
        except jwt.ExpiredSignatureError:
            return Response(
                {"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED
            )
        try:
            client = Client.objects.get(id=clientId)
        except Client.DoesNotExist:
            return Response(
                {"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            subscription = Subscription.objects.get(client=client)
        except Subscription.DoesNotExist:
            return Response(
                {"Error": "Client non souscrite"}, status=status.HTTP_404_NOT_FOUND
            )
        subscription.renew_status = request.data["renew"]
        subscription.save()
        return Response({"status": "Subscription renew status updated"})
    return Response({"Error": "There is no data"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def share_linkedin(request):
    if "language" in request.query_params:
        language = request.query_params["language"]
        if language in ["fr", "en"]:
            if language == "fr":
                translation.activate(language)
            if language == "en":
                translation.activate(language)
    try:
        clientId = jwt.decode(
            get_request_token(request),
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
        )["id"]
    except jwt.ExpiredSignatureError:
        return Response({"Error": TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        client = Client.objects.get(id=clientId)
    except Client.DoesNotExist:
        return Response({"Error": CLIENT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    if request.data["code"] == client.storage_code_client:
        params = {
            "grant_type": "authorization_code",
            "code": request.data["parsed_code"],
            "client_id": "78v3ljq07zd626",
            "client_secret": "lFnKGgxKMdL4VO26",
            "redirect_uri": os.environ.get("FRONT_URL"),
        }
        linkedin_auth = requests.post(LINKEDIN_AUTH_LINK, params=params)
        if linkedin_auth.status_code == 200:
            token = linkedin_auth.json()["access_token"]
            headers = {"Authorization": "Bearer " + token}
            linkedin_token = requests.get(LINKEDIN_API_URL + "/me", headers=headers)
            if linkedin_token.status_code == 200:
                msg_1 = gettext("Use my code")
                msg_2 = gettext("to get free days and credits on Predict Market")
                payload = {
                    "author": f"urn:li:person:{linkedin_token.json()['id']}",
                    "lifecycleState": "PUBLISHED",
                    "specificContent": {
                        "com.linkedin.ugc.ShareContent": {
                            "shareCommentary": {
                                "text": f"{msg_1} {request.data['code']} {msg_2}",
                            },
                            "shareMediaCategory": "ARTICLE",
                            "media": [
                                {
                                    "status": "READY",
                                    "description": {
                                        "text": "Use our code descrption",
                                    },
                                    "originalUrl": os.environ.get("FRONT_URL"),
                                    "title": {
                                        "text": "Official LinkedIn Blog",
                                    },
                                },
                            ],
                        },
                    },
                    "visibility": {
                        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC",
                    },
                }
                publish_linkedin = requests.post(
                    LINKEDIN_API_URL + "/ugcPosts",
                    data=json.dumps(payload),
                    headers=headers,
                )
                if publish_linkedin.status_code == 201:
                    return Response({"status": "Linkedin post shared"})
        return Response(
            {"Error": "Linkedin post not shared"}, status=status.HTTP_400_BAD_REQUEST
        )
    return Response({"Error": "Data error"}, status=status.HTTP_400_BAD_REQUEST)
