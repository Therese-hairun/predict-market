import base64
import binascii
import datetime
import os

import jwt
import requests
import re
from market.config import CREDIT_PERCENT, FAKE_MAIL, TOKEN_MAX_AGE
import re
from natsort import natsorted

from predict.constant import LIST_12H, LIST_2H, LIST_4H, LIST_6H


def fakemail(mail: str) -> bool:
    if mail[mail.index("@") + 1 :] in FAKE_MAIL:
        return True
    else:
        return False


def generate_token(clientId, admin=False):
    if admin:
        id_key = "admin_id"
    else:
        id_key = "id"
    payload = {
        id_key: clientId,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_MAX_AGE),
        "iat": datetime.datetime.utcnow(),
    }
    token: bytes = jwt.encode(
        payload, os.environ.get("SECRET_KEY"), algorithm="HS256"
    ).decode("utf-8")
    return {"token": token, "exp": datetime.datetime.utcfromtimestamp(payload["exp"])}


def format_amount(amount):
    return int(amount * 100)


def get_credit_percentage(credit):
    return credit * CREDIT_PERCENT / 100


def encode_multipart_formdata(fields):
    boundary = binascii.hexlify(os.urandom(16)).decode("ascii")

    body = (
        "".join(
            "--%s\r\n"
            'Content-Disposition: form-data; name="%s"\r\n'
            "\r\n"
            "%s\r\n" % (boundary, field, value)
            for field, value in fields.items()
        )
        + "--%s--\r\n" % boundary
    )

    content_type = "multipart/form-data; boundary=%s" % boundary

    return body, content_type


def find_first_interval(intervals):
    return intervals.split(",")[0].replace("[", "").replace("]", "").replace("'", "")


def check_training_state(state):
    return state == "done"


def get_training_state(state1, state2, state3):
    if (
        check_training_state(state1)
        and check_training_state(state2)
        and check_training_state(state3)
    ):
        return "Terminé"
    else:
        return "En cours"


def to_time_stamp(d: datetime):
    return int(datetime.datetime.timestamp(d))


def get_precision(symbol, interval):
    date = datetime.datetime.utcnow()
    data = encode_multipart_formdata(
        {
            "symbol": symbol,
            "start": to_time_stamp(date - datetime.timedelta(hours=24)),
            "end": to_time_stamp(date),
            "interval": interval,
        }
    )
    reqUrl = os.environ.get("API_PREDICTION_URL") + "hist_prediction_accuracy"
    response = requests.request(
        "POST", reqUrl, data=data[0], headers={"Content-Type": data[1]}
    )
    result = response.json()
    return ((result["close"] + result["high"] + result["low"]) / 3) * 100


def format_h24(h24):
    return ("+" if h24 > 0 else "") + "{:.2f}".format(h24)


def dict2obj(d):
    if isinstance(d, list):
        d = [dict2obj(x) for x in d]
    if not isinstance(d, dict):
        return d

    class C(object):
        pass

    o = C()
    for k in d:
        o.__dict__[k] = dict2obj(d[k])
    return o


def format_interval(intervals):
    return ";".join(
        intervals.replace("[", "").replace("]", "").replace("'", "").split(",")
    )


def get_request_token(request):
    return request.META.get("HTTP_AUTHORIZATION").split()[1]


def replaceTextBetween(originalText, delimeterA, delimterB, replacementText):
    leadingText = originalText.split(delimeterA)[0]
    trailingText = originalText.split(delimterB)[1]

    return leadingText + delimeterA + replacementText + delimterB + trailingText


def validate_password(password):
    pattern = re.compile(
        "^(?=.*[a-z].*[A-Z]|[A-Z].*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    )
    return pattern.match(password) != None


def sort_interval(intervals):
    intervals = intervals.split(";")
    minutes = natsorted([i for i in intervals if "m" in i])
    hours = natsorted([i for i in intervals if "h" in i])
    days = natsorted([i for i in intervals if "d" in i])
    return minutes + hours + days

def to_timestamp_milliseconds(date:datetime):
    return int((datetime.datetime.timestamp(date) *1000)-1)

def round_time(time, round_to):
    rounded = time + datetime.timedelta(minutes=round_to/2.)
    rounded -= datetime.timedelta(minutes=rounded.minute % round_to,
                                  seconds=rounded.second,
                                  microseconds=rounded.microsecond)
    return rounded

def make_filter_interval(interval:str,limit):
    initial=interval[-1]
    interval_number=int(interval[0:-1])
    res=[]
    date_now=datetime.datetime.utcnow()
    multiplicator=0
    if initial == "m":
        res.append(to_timestamp_milliseconds(round_time(date_now,interval_number)))
        multiplicator=60*1000
        limit-=1
    elif initial =="h":
        res.append(to_timestamp_milliseconds(round_time(date_now.replace(minute=0,second=0,microsecond=0,hour=date_now.hour+1),interval_number)))
        multiplicator=3600*1000
        limit-=1
    elif initial=="d":
        res.append(to_timestamp_milliseconds(round_time(date_now.replace(minute=0,second=0,microsecond=0,hour=0),interval_number)))
        multiplicator=24*3600*1000
    for i in range(0,limit):
        res.append(res[i]-(interval_number*multiplicator))
    return tuple(res)

def round_minutes(dt:datetime.datetime, interval:str):
    initial=interval[-1]

    if initial=="m": 
        minute_rounded=int(interval[0:-1])
        new_minute = (dt.minute // minute_rounded) * minute_rounded
        return dt + datetime.timedelta(minutes=new_minute - dt.minute)
    elif initial =="h":
        return dt.replace(hour=round_hours(dt=dt,interval=interval),minute=0,second=0,microsecond=0)
    elif initial =="d":
        return dt.replace(minute=0,second=0,microsecond=0,hour=0)

def substract_time(interval:str,endtimestamp):
    if interval[-1]=="m":
        return endtimestamp-(int(interval[0:-1])* 60*1000)
    elif interval[-1]=="h":
        return endtimestamp-(int(interval[0:-1])* 3600*1000)
    elif interval[-1]=="d":
        return endtimestamp-(int(interval[0:-1])*24* 3600*1000)
    
def round_hours(dt: datetime.datetime,interval:str):
    hour_list=[]
    if int(interval[0:-1])==2:
        hour_list=LIST_2H
    elif int(interval[0:-1])==4:
        hour_list=LIST_4H
    elif int(interval[0:-1])==6:
        hour_list=LIST_6H
    elif int(interval[0:-1])==12:
        hour_list=LIST_12H
    else :
        return dt.hour
    min_hour = [abs(dt.hour - hour) for hour in hour_list]
    return hour_list[min_hour.index(min(min_hour))]