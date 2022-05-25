# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.deletion import CASCADE


class Admin(models.Model):

    email = models.EmailField(unique=True, max_length=80)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    is_super_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "admin"

    @property
    def info(self):
        return {"id": self.id, "username": self.username}


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "authtoken_token"


class Reward(models.Model):

    sum = models.FloatField(blank=True, null=True)
    free_day = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    total_for_next_subscription = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "reward"

    @property
    def info(self):
        return {"sum": self.sum, "free_day": self.free_day}


class Client(models.Model):

    relationship_code = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    email_validation_code = models.CharField(max_length=255, blank=True, null=True)
    sms_validation_code = models.CharField(max_length=255, blank=True, null=True)
    email_is_activated = models.BooleanField(default=False)
    phone_is_activated = models.BooleanField(default=False)
    account_is_active = models.BooleanField(default=False)
    token = models.CharField(max_length=255, blank=True, null=True)
    storage_code_client = models.CharField(
        max_length=255, blank=True, null=True, unique=True
    )
    total_day = models.IntegerField(blank=True, null=True)
    reward = models.ForeignKey(Reward, models.DO_NOTHING)
    login_attempted_error = models.DateTimeField(blank=True, null=True)
    customers_id = models.CharField(max_length=255, blank=True, null=True)
    profil = models.ImageField(
        upload_to="user_profile", null=True, blank=True, max_length=255
    )

    class Meta:
        managed = True
        db_table = "client"

    def __str__(self):
        return "%d:%s %s" % (self.id, self.lastname, self.firstname)

    @property
    def full_name(self):
        return {"id": self.id, "full_name": self.firstname + " " + self.lastname}

    @property
    def info(self):
        return {
            "id": self.id,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "account_status": self.account_is_active,
            "reward": {"sum": self.reward.sum, "free_day": self.reward.free_day},
        }

    @property
    def infoAndMail(self):
        return {
            "id": self.id,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "account_status": self.account_is_active,
            "email": self.email,
            "reward": {"sum": self.reward.sum, "free_day": self.reward.free_day},
        }

    @property
    def ClientName(self):
        return self.firstname + " " + self.lastname


class ClientPhone(models.Model):

    client = models.ForeignKey(Client, models.DO_NOTHING)
    number = models.CharField(max_length=255, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sms_code = models.CharField(max_length=255, blank=True, null=True)
    sms_date = models.DateTimeField(blank=True, null=True)
    sms_expiry = models.DateTimeField(blank=True, null=True)
    is_phone_active = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = "client_phone"


class ClientToken(models.Model):

    client = models.ForeignKey(Client, models.DO_NOTHING)
    token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    token_expiry = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "client_token"


class Couple(models.Model):

    symbol_1 = models.CharField(max_length=255, blank=True, null=True)
    symbol_1_logo = models.ImageField(
        upload_to="symbol_crypto", null=True, blank=True, max_length=255
    )
    symbol_2 = models.CharField(max_length=255, blank=True, null=True)
    symbol_2_logo = models.ImageField(
        upload_to="symbol_crypto", null=True, blank=True, max_length=255
    )
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    status = models.BooleanField(default=True)
    intervals = models.CharField(max_length=100, blank=True, null=True)
    vues = models.IntegerField(default=0, blank=True, null=True)
    precision = models.FloatField(default=0.0, blank=True, null=True)
    is_authorised = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "couple"

    @property
    def coupleName(self):
        return self.name


class CoupleAuthorized(models.Model):

    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    couple = models.ForeignKey(Couple, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "couple_authorized"


class CoupleDemand(models.Model):
    clients = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    couple = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "couple_demand"


class CoupleFavorite(models.Model):

    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    couple = models.ForeignKey(Couple, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "couple_favorite"


class CoupleVue(models.Model):
    couple = models.ForeignKey(Couple, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "couple_vue"


class CoupleData(models.Model):
    couple = models.ForeignKey(Couple, null=True, blank=True, on_delete=models.CASCADE)
    enddatetime = models.DateTimeField()
    intervaltime = models.CharField(max_length=10)
    high = models.DecimalField(max_digits=50, decimal_places=10)
    low = models.DecimalField(max_digits=50, decimal_places=10)
    close = models.DecimalField(max_digits=50, decimal_places=10)
    open = models.DecimalField(max_digits=50, decimal_places=10)
    volume = models.DecimalField(max_digits=50, decimal_places=10)

    class Meta:
        managed = True
        db_table = "couple_data"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class History(models.Model):

    admin = models.ForeignKey(Admin, models.DO_NOTHING, default=1)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    credit_initial_user = models.FloatField(blank=True, null=True)
    credit_added_user = models.DateTimeField(blank=True, null=True)
    credit_deleted_user = models.FloatField(blank=True, null=True)
    credit_final_user = models.FloatField(blank=True, null=True)
    total_day_initial_user = models.IntegerField(blank=True, null=True)
    day_added_user = models.IntegerField(blank=True, null=True)
    day_deleted_user = models.IntegerField(blank=True, null=True)
    total_day_final_user = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "history"


class Invoice(models.Model):

    payment = models.ForeignKey("Payment", models.DO_NOTHING)
    initial_price = models.FloatField(blank=True, null=True)
    discount_credit = models.FloatField(blank=True, null=True)
    discount_code = models.FloatField(blank=True, null=True)
    final_price = models.FloatField(blank=True, null=True)
    nb_crypto_currency = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "invoice"


class KnoxAuthtoken(models.Model):
    digest = models.CharField(primary_key=True, max_length=128)
    salt = models.CharField(unique=True, max_length=16)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    expiry = models.DateTimeField(blank=True, null=True)
    token_key = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = "knox_authtoken"


class Payment(models.Model):

    subscription = models.ForeignKey("Subscription", models.DO_NOTHING)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "payment"

    @property
    def info(self):
        return {
            "reference": self.reference,
            "subscribe": self.subscription.subscribe.info,
            "echeance": self.subscription.end,
        }


class RelationshipCode(models.Model):

    client = models.ForeignKey(Client, models.DO_NOTHING)
    code = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "relationship_code"


###GESTION PARAINAGE ######
class SimpleRewardByRelationshipCode(models.Model):

    client_child_name = models.ForeignKey(Client, models.DO_NOTHING)
    reward_day_by_child = models.IntegerField(default=0, blank=True, null=True)
    reward_credit_by_child = models.FloatField(default=0.0, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "simple_reward_by_relationship_code"


class Subscribe(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    reduction = models.FloatField(blank=True, null=True)
    number_couple_offered = models.BigIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    recommanded = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = "subscribe"

    def __str__(self):
        return "%d:%s" % (self.id, self.name)

    @property
    def info(self):
        return {
            "id": self.id,
            "name": self.name,
            "number_couple_offered": self.number_couple_offered,
        }


class CodeReductionAvailable(models.Model):
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    expiry_at = models.DateTimeField(blank=True, null=True)
    client_is_subscribed = models.BooleanField(default=False)
    reduction = models.FloatField(blank=True, null=True)
    clients = models.ManyToManyField(Client, blank=True, null=True)
    subscribes = models.ManyToManyField(Subscribe, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "code_reduction_available"


class CodeReductionUsed(models.Model):

    code_used = models.ForeignKey(CodeReductionAvailable, models.DO_NOTHING)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    code = models.CharField(max_length=255, blank=True, null=True)
    used_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "code_reduction_used"


class Subscription(models.Model):

    client = models.ForeignKey(Client, models.DO_NOTHING)
    subscribe = models.ForeignKey(Subscribe, models.DO_NOTHING)
    couples = models.ManyToManyField(Couple, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    renew_status = models.BooleanField(blank=True, null=True)
    total_discount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    activate = models.BooleanField(blank=True, null=True)
    payment_method_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "subscription"


class CoupleHistory(models.Model):
    couple = models.ForeignKey(Couple, models.DO_NOTHING)
    subscription = models.ForeignKey(Subscription, models.DO_NOTHING)
    couple_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "couple_history"


class TastypieApiaccess(models.Model):
    id = models.BigAutoField(primary_key=True)
    identifier = models.CharField(max_length=255)
    url = models.TextField()
    request_method = models.CharField(max_length=10)
    accessed = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "tastypie_apiaccess"


class TastypieApikey(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=128)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "tastypie_apikey"


class Ticket(models.Model):

    client = models.ForeignKey(Client, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = "ticket"


class TicketMessage(models.Model):

    ticket = models.ForeignKey(Ticket, models.DO_NOTHING)
    author = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    date_message = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = "ticket_message"


class ClientDowngrade(models.Model):

    client = models.ForeignKey(Client, models.DO_NOTHING)
    renew = models.DateTimeField()
    subscribe = models.ForeignKey(Subscribe, models.DO_NOTHING)
    duration = models.IntegerField(blank=True, null=True)
    total_discount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_created=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payment_method_id = models.CharField(max_length=255, blank=True, null=True)
    couples = models.ManyToManyField(Couple, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "client_downgrade"


class SMS(models.Model):
    send_at = models.DateTimeField(auto_now_add=True)
    sender_ip = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "sms"
