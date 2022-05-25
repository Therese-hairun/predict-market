from itertools import count
from rest_framework import serializers
from market.config import TVA

from prediction.models import Asset
from .models import (
    Admin,
    Client,
    ClientPhone,
    CodeReductionAvailable,
    CoupleAuthorized,
    CoupleFavorite,
    CoupleVue,
    Invoice,
    SimpleRewardByRelationshipCode,
    Subscribe,
    Subscription,
    Reward,
    Couple,
    CoupleDemand,
    Couple,
    Ticket,
    TicketMessage,
)

from drf_api_logger.models import APILogsModel


class ClientSerializer(serializers.ModelSerializer):
    def get_first_name(self, obj):
        # obj is model instance
        return obj.firstname

    class Meta:
        model = Client
        fields = "__all__"


class SubcribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPhone
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class CodeReductionAvailableSerializer(serializers.ModelSerializer):
    clients = serializers.SlugRelatedField(
        slug_field="full_name", many=True, read_only=True
    )
    subscribes = serializers.SlugRelatedField(
        slug_field="info", many=True, read_only=True
    )

    class Meta:
        model = CodeReductionAvailable
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field="info", many=False, read_only=True)
    subscribe = serializers.StringRelatedField(many=False)

    class Meta:
        model = Subscription
        exclude = ("couples", "payment_method_id")


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = "__all__"


class SubscriptionWithEmailSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field="infoAndMail", many=False, read_only=True
    )
    subscribe = serializers.SlugRelatedField(
        slug_field="info", many=False, read_only=True
    )
    number_couple = serializers.SerializerMethodField()
    profil = serializers.SerializerMethodField()
    number_of_affiliated = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        exclude = ("couples", "payment_method_id")

    @classmethod
    def get_number_couple(self, obj):
        return obj.couples.all().count()

    def get_profil(self, object):
        request = self.context.get("request")
        print(request)
        profil_url = "images/" + str(object.client.profil)
        return request.build_absolute_uri("/") + (profil_url)

    def get_number_of_affiliated(self, object):
        return Client.objects.filter(
            relationship_code=object.client.storage_code_client
        ).count()


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    payment = serializers.SlugRelatedField(
        slug_field="info", many=False, read_only=True
    )
    TVA = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = "__all__"

    @classmethod
    def get_TVA(self, object):
        return float("{:.2f}".format((object.initial_price / (1 + TVA)) * TVA))


class ClientByTokenSerializer(serializers.ModelSerializer):
    reward = serializers.SlugRelatedField(slug_field="info", many=False, read_only=True)
    subscription = serializers.SerializerMethodField()
    profil = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = (
            "id",
            "firstname",
            "lastname",
            "email",
            "phone",
            "storage_code_client",
            "relationship_code",
            "reward",
            "subscription",
            "profil",
        )

    def get_subscription(self, object):
        subscription = Subscription.objects.get(client=object)
        price = subscription.subscribe.price - (
            (subscription.subscribe.price * subscription.subscribe.reduction) / 100
        )
        if subscription.duration == 365:
            price *= 12
        return {
            "id": subscription.subscribe.id,
            "name": subscription.subscribe.name,
            "end": subscription.end,
            "number_couple_offered": subscription.subscribe.number_couple_offered,
            "number_couple": subscription.couples.all().count(),
            "activate": subscription.activate,
            "renew_status": subscription.renew_status,
            "price": price,
        }

    def get_profil(self, object):
        request = self.context.get("request")
        profil_url = "images/" + str(object.profil)
        return request.build_absolute_uri("/") + (profil_url)


class CoupleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Couple
        exclude = ("intervals",)


class CoupleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Couple
        exclude = ("intervals",)


class CoupleInfoSerializer(serializers.ModelSerializer):
    is_used = serializers.SerializerMethodField()

    class Meta:
        model = Couple
        fields = "__all__"

    @classmethod
    def get_is_used(self, obj):
        subscription = Subscription.objects.values("couples")
        for i in subscription:
            if i["couples"] == obj.id:
                return True
        return False


class CoupleDemandSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    last_date = serializers.DateTimeField()

    class Meta:
        model = CoupleDemand
        fields = ("count", "couple", "last_date")


class CoupleAuthorisedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoupleAuthorized
        fields = "__all__"


class CoupleFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoupleFavorite
        fields = "__all__"


class CoupleFavoriteInfoSerializer(serializers.ModelSerializer):
    symbol = serializers.SerializerMethodField()
    coupleId = serializers.SerializerMethodField()
    fullName = serializers.SerializerMethodField()
    symbol_1_logo = serializers.SerializerMethodField()
    symbol_2_logo = serializers.SerializerMethodField()

    class Meta:
        model = CoupleFavorite
        fields = ("symbol", "coupleId", "fullName", "symbol_1_logo", "symbol_2_logo")

    @classmethod
    def get_symbol(self, object):
        return object.couple.name

    def get_coupleId(self, object):
        return object.couple.id

    def get_fullName(self, object):
        asset1 = Asset.objects.using("crypto").get(assetname=object.couple.symbol_1)
        asset2 = Asset.objects.using("crypto").get(assetname=object.couple.symbol_2)

        return asset1.assetfullname + "/" + asset2.assetfullname

    def get_symbol_1_logo(self, object):
        url = object.couple.symbol_1_logo.url
        return url

    def get_symbol_2_logo(self, object):
        url = object.couple.symbol_2_logo.url
        return url


class CreateTicketMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketMessage
        fields = "__all__"


class TicketMessageSerializer(serializers.ModelSerializer):
    message_date = serializers.SerializerMethodField()
    message_time = serializers.SerializerMethodField()

    class Meta:
        model = TicketMessage
        fields = [
            "author",
            "message",
            "date_message",
            "is_admin",
            "message_date",
            "message_time",
        ]

    @classmethod
    def get_message_date(self, object):
        return object.date_message.date()

    def get_message_time(self, object):
        return object.date_message.time()


class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field="info", many=False, read_only=True)
    last_change = serializers.SerializerMethodField()

    @classmethod
    def get_last_change(self, object):
        message = TicketMessage.objects.filter(ticket=object.id).last()
        if message:
            return message.date_message
        return message

    class Meta:
        model = Ticket
        fields = "__all__"


class ClientRewardSerializer(serializers.ModelSerializer):
    client_child_name = serializers.SlugRelatedField(
        slug_field="ClientName", many=False, read_only=True
    )

    class Meta:
        model = SimpleRewardByRelationshipCode
        fields = "__all__"


class CoupleVueSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = CoupleVue
        fields = ("count",)


# Log
class ApiLogsSeralizer(serializers.ModelSerializer):
    class Meta:
        model = APILogsModel
        fields = "__all__"
