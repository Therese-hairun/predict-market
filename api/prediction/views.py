import datetime
import os
import requests
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from predict.utils import (
    check_training_state,
    encode_multipart_formdata,
    get_training_state,
    to_time_stamp,
)

from prediction.serializers import AssetSerializer, SymbolSerializer, TrainingSerializer
from .models import Asset, Symbol, Training
from rest_framework.response import Response


class ApiAssetListView(ListAPIView):
    queryset = Asset.objects.using("crypto").exclude(active=False).order_by("assetname")
    serializer_class = AssetSerializer


class ApiSymbolListView(ListAPIView):
    queryset = Symbol.objects.using("crypto").all()
    serializer_class = SymbolSerializer


from django.db.models import Count


@api_view(["GET"])
def get_training(request, symbol):
    training = Training.objects.using("crypto").filter(symbolid__symbol=symbol)

    intervalTimes = (
        Training.objects.using("crypto")
        .filter(symbolid__symbol=symbol)
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
        result[index]["precision"] = get_precision(symbol, interval["intervaltime"])
        result[index]["interval"] = interval["intervaltime"]
        index += 1
    return Response({"data": result})


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
