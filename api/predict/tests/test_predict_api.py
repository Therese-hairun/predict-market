import json
from os import access
from django.http import response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.test import TestCase

# from django.test import Client
from django.urls import reverse, resolve
from ..models import (
    Admin,
    Client,
    ClientToken,
    CodeReductionAvailable,
    Couple,
    Reward,
    Ticket,
)
import jwt, os
from ..serializers import (
    AdminSerializer,
    ClientSerializer,
    CodeReductionAvailableSerializer,
    CoupleSerializer,
)
import stripe

from predict.views import (
    ApiClientFilleulListView,
    ApiClientTicketListView,
    ApiLogsList,
    ApiSubscriptionListView,
    ApiTicketListView,
    add_couple_for_visualisation,
    add_credit_to_subscription,
    add_days_to_subscription,
   # add_reward, 
    add_subscribe,
    change_cusomer_status,
    change_validated_status,
    check_downgrade,
    create_client,
    create_couple,
    create_ticket,
    create_ticket_message,
    generateAuthToken,
    get_all_couple,
    get_by_subscribe_id,
    get_client_favorite_couple,
    #get_confirmation_code,
    get_couple_prediction,
    get_reward_by_id,
    get_user_by_token,
    login,
    payement,
    remove_couple_for_visualisation,
    reset_password,
    send_mail,
    send_sms,
    ticket_details,
    #update_client,
    update_client_general_info,
    update_email_status,
    update_reward,
    update_password,
    update_phone_status,
    update_reward_free_day,
    update_subscribe,
    update_subscribe_status,
    upload_user_profil,
    verify_account,
    verify_phone,
    verify_token,
)
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient, URLPatternsTestCase

from django.conf import settings
from datetime import datetime
import jwt

from predict import serializers
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# initialize the APIClient app
# client = Client()
client = APIClient()



class UrlTest(TestCase):
    def test_get_user_list_is_resolved(self):
        url = reverse("user_list")
        # print("Absolute url for registration: ", url)

        self.assertEquals(resolve(url).func.view_class, ApiSubscriptionListView)
        # print(resolve(url))
    def test_get_user_by_token_is_resolved(self):
        url = reverse("customer_by_id")
        # print("Absolute url for registration: ", url) 

        self.assertEquals(resolve(url).func, get_user_by_token)
        # print(resolve(url))
    def test_get_url_for_payment_is_resolved(self):
        url = reverse("payement")
        # print("Absolute url for registration: ", url) 

        self.assertEquals(resolve(url).func, payement)
        # print(resolve(url))
    def test_get_url_update_password_is_resolved(self):
        url = reverse("update_password")
        # print("Absolute url for registration: ", url)  

        self.assertEquals(resolve(url).func, update_password)
        # print(resolve(url))
    
    def test_get_url_update_customer_status_is_resolved(self):
        url = reverse("account_status", kwargs={'id':1})
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, change_cusomer_status)  
        # print(resolve(url))
    
    def test_get_url_activate_phone_status_is_resolved(self):
        url = reverse("activate_phone")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, update_phone_status )  
        # print(resolve(url))
    def test_get_url_activate_email_status_is_resolved(self):
        url = reverse("activate_email")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, update_email_status)  
        # print(resolve(url))
    
    def test_get_url_update_customer_infos_is_resolved(self):
        url = reverse("update_client_infos")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, update_client_general_info)  
        # print(resolve(url))

    def test_get_url_to_upload_profil_is_resolved(self):
        url = reverse("upload_user_profil")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, upload_user_profil)  
        # print(resolve(url))
    
    def test_get_url_to_send_email_is_resolved(self):
        url = reverse("send_mail")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, send_mail)  

        # print(resolve(url))
    
    def test_get_url_to_send_sms_is_resolved(self):
        url = reverse("send_sms")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, send_sms)  
        
        # print(resolve(url))
    
    def test_get_url_to_verify_phone_is_resolved(self):
        url = reverse("verify_phone")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, verify_phone)  
    
    
    def test_get_url_to_reset_pasword_is_resolved(self):
        url = reverse("reset_password")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func,  reset_password)  
    def test_get_url_to_verify_phone_is_resolved(self):
        url = reverse("verify_phone")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, verify_phone)  
    
    def test_get_url_to_verify_account_is_resolved(self):
        url = reverse("verify_account")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, verify_account)  
    def test_get_url_to_verify_token_is_resolved(self):
        url = reverse("verify_token")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, verify_token)  
    def test_get_url_for_generating_token_is_resolved(self):
        url = reverse("generate_token")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, generateAuthToken) 
   
    def test_get_absolute_url_for_register(self): 
        url = reverse("create_client")
        # print("Absolute url for registration: ", url)
        self.assertEquals(resolve(url).func, create_client)
        # print(resolve(url))
  

    def test_get_absolute_url_for_login(self):
        url = reverse("login")
        # print(" Absolute url for login: ", url)
        self.assertEquals(resolve(url).func, login)
        # print(resolve(url))

    def test_client_registration_is_resolved(self):
        url = reverse("create_client")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, create_client)

    def test_couple_registration_is_resolved(self):
        url = reverse("create_couple")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, create_couple)

###
    def test_ubscribe_registration_resolved(self):
        url = reverse("add_subscribe")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, add_subscribe)

    def test_get_subscribe_is_resolved(self):
        url = reverse("get_subcribe_by_id", kwargs={"id": 1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, get_by_subscribe_id)

    def test_subscribe_is_resolved(self):
        url = reverse("update_subscribe", kwargs={"id": 1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, update_subscribe)
        
##
    def test_add_credit_to_subscrib_is_resolved(self):
        url = reverse("add_credits_to_subscription")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, add_credit_to_subscription)

    def test_update_subscribe_status_is_resolved(self):
        url = reverse("update_subscribe_status", kwargs={"id": 1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, update_subscribe_status)
##
    def test_get_reward__is_resolved(self):
        url = reverse("get_reward_by_id", kwargs={"id": 1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, get_reward_by_id)

    def test_update_reward_credit_is_resolved(self):
        url = reverse("update_reward_credit", kwargs={"id": 1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, update_reward)

    def test_update_free_day_is_resolved(self):
        url = reverse("update_reward_day", kwargs={"id": 1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, update_reward_free_day)

    def test_create_ticket_is_resolved(self):
        url = reverse("create_ticket")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, create_ticket)

    def test_get_clients_ticket_is_resolved(self):
        url = reverse("get_client_tickets")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func.view_class, ApiClientTicketListView)
        ##
    def test_get_clients_FILLEUL_is_resolved(self):
        url = reverse("get_client_filleul", kwargs={"code": "M244"})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func.view_class, ApiClientFilleulListView)

    def test_get_ticket_detail_is_resolved(self):
        url = reverse("get_ticket_details", kwargs={"id": 1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, ticket_details)

    def test_get_ALL_ticket_is_resolved(self):
        url = reverse("get_all_tickets")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func.view_class, ApiTicketListView)

##
    def test_create_ticket_message_is_resolved(self):
        url = reverse("create_ticket_message", kwargs={"id": 1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, create_ticket_message)

    def test_get_all_couple_is_resolved(self):
        url = reverse("get_all_couple")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, get_all_couple)

    def test_get_couple_prediction_is_resolved(self):
        url = reverse("get_couple_prediction", kwargs={"symbol": "BTCUSD"})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, get_couple_prediction)

    def test_get_favorite_couple_is_resolved(self):
        url = reverse("get_client_favorite_couple")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, get_client_favorite_couple)
        ###

    def test_add_couple_for_viz_is_resolved(self):
        url = reverse("add_couple_for_visualisation")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, add_couple_for_visualisation)

    def test_remove_couple_for_viz_is_resolved(self):
        url = reverse("remove_couple_for_visualisation")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, remove_couple_for_visualisation)

    def test_add_credit_for_sub_is_resolved(self):
        url = reverse("add_credits_to_subscription")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, add_credit_to_subscription)

    def test_add_days_for_subscription_is_resolved(self):
        url = reverse("add_days_to_subscription")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, add_days_to_subscription)
    
    def test_get_url_for_log_is_resolved(self):
        url = reverse("api_log")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func.view_class, ApiLogsList)
    def test_get_url_for_checking_downgrade_is_resolved(self):
        url = reverse("check_downgrade")
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, check_downgrade)
  
    def test_get_url_for_checking_couple_validate_is_resolved(self):
        url = reverse("change_couple_validation_state", kwargs={'id':1})
        # print(resolve(url).func)
        self.assertEquals(resolve(url).func, change_validated_status )
  
    
    
class CreateSuperAdmin(TestCase):
    def test_api_jwt(self):

        url_create_admin = reverse("create_admin")
        url_login = reverse("login")
        url_get_admin = reverse("get_admin")

        # print(url_get_admin)
        self.assertEqual(url_get_admin, "/api/admin")
        self.assertEqual(url_create_admin, "/api/create_admin")
        self.assertEqual(url_login, "/api/login")  

        # url_detail = reverse('get_admin')
        # u = user_model.objects.create_user(username='user', email='user@foo.com', password='pass')

        u = Admin.objects.create(
            username="MI",
            email="chri@hairun-technology.com",
            password="Admin123!!",
            # is_super_admin = True,
            is_admin=True,
        )
        # u.is_active = False

        u.is_super_admin = False
        u.save()
        #print(u.token)  

        # resp = self.client.post(url, {'email':'user@foo.com', 'password':'pass'}, format='json')
        resp = self.client.post(
            url_create_admin, 
            {"username": "MIJA", "email": "krkrkr@gmail.com", "password": "Admin123!"},
            content_type="application/json",
        )
        ###self.assertEqual(resp.status_code, status.HTTP_200_OK) 

        # u.is_active = True
        u.is_super_admin = True
        u.save()

        # resp = self.client.post(url, {'username':'user@foo.com', 'password':'pass'}, format='json')
        resp = self.client.post(
            url_login,
            {"email": "chri@hairun-technology.com", "password": "Admin123!!"},
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        ###print(resp.data) 
        ##self.assertTrue('token' in resp.data)
        ## token = resp.data['token']
       # self.assertTrue("adminToken" in resp.data)
        ##admin_token = resp.data["adminToken"]
        ##print("AdminToken:", admin_token)

        ###
        """
        client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(admin_token))
        response = self.client.get(reverse('get_admin', args=[1]), data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        """

        ##def test_get_admin(self):
        # id = jwt.decode(pk, os.environ.get("SECRET_KEY"), algorithms="HS256")["id"]
        ##client.credentials(HTTP_AUTHORIZATION="JWT " + admin_token)
        ## resp = client.get('/api/v1/account/', data={'format': 'json'})
        """
        resp = self.client.get('/api/admin/1') 
        self.assertEqual(resp.status_code, status.HTTP_200_OK) 
            """
        super_admin = Admin.objects.get(pk=1)
        serializer = AdminSerializer(super_admin)
        # self.assertEqual(response.data, serializer.data)
        ###self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # print(resp.data)

    """

        verification_url = reverse('api-jwt-verify')
        resp = self.client.post(verification_url, {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK) 

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
        resp = client.get('/api/v1/account/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        resp = client.get('/api/v1/account/', data={'format': 'json'})j
        
    """


class CreateClientTest(TestCase):
    def test_api_jwt_credentials(self):

        url = reverse("create_client")
        url_login = reverse("login")
        url_ticket = reverse("create_ticket")
        url_get_admin = reverse("get_admin")
        # u = user_model.objects.create_user(username='user', email='user@foo.com', password='pass')

        r = Reward.objects.create(sum="10.0")

        u = Client.objects.create(
            firstname="MIIJ",
            email="mchristian@hairun-technology.com",
            password="Admin123!!!",
            # is_super_admin = True,
            phone="+261341261032",
            reward=r,
        )
        # u.is_active = False

        u.email_is_activated = True

        u.phone_is_activated = True
        u.account_is_active = True
        u.save()

       
        # resp = self.client.post(url, {'username':'user@foo.com', 'password':'pass'}, format='json')
       ## resp = self.client.post(
          ##  url_login,
           ## {"email": "chris@gmail.com", "password": "Admin123!"},
            ##content_type="application/json",
       ## )
        ##self.assertEqual(resp.status_code, status.HTTP_200_OK)
       ## print(resp.data)
        ##self.assertTrue('token' in resp.data)
        ## token = resp.data['token']
       ## self.assertTrue("token" in resp.data)
       ## client_token = resp.data["token"]
       ## print("ClienToken:", client_token)

        ####TICKET USER #####
        """
        data = {
            'token': client_token,
            'client':u.id,
            'name':'HAIRUN',
            'created_at': datetime.utcnow()

        }
        response = self.client.post(url_ticket, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        """

        # print(resp.data)

    """  
        verification_url = reverse('api-jwt-verify')
        resp = self.client.post(verification_url, {'token': token}, format='json') 
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')  
        resp = client.get(url_get_admin, data={'format': 'json'}) 
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + client_token)
        resp = client.get(url_get_admin, data={'format': 'json'}) 
        self.assertEqual(resp.status_code, status.HTTP_200_OK)  
   
   

    def test_get_all_clients(self):
        # get API response
        response = self.client.get(reverse("user_list"))
        # get data from db
        experiments = Client.objects.all()
        serializer = ClientSerializer(experiments, many=True)
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

 """
 
class ProfilTestCase(TestCase):
    all_ = reverse("user_list")

    def setUp(self):
        self.r = Reward.objects.create(sum="10.0")

        self.u = Client.objects.create(
            firstname="MIIJ",
            email="mijachristian@hairun-technology.com",
            password="Admin123!!!",
            # is_super_admin = True,
            phone="+261345161032",
            reward=self.r,
        )

        self.user = User.objects.create(username="ChristianDS", password="Qwerty123!!")
        self.token = Token.objects.create(user=self.user)

    def api_athentification(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token" + self.token)

    def test_user_is_authenticated(self):

        response = self.client.get(self.all_) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)   


class TestSubscription(TestCase):
    def test_add_subscribe(self):
        response = self.client.post(
            reverse("add_subscribe"),
            {"name": "GOLD", "price": "10.00"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_subscribe(self):

        response = self.client.patch(
            reverse("update_subscribe", kwargs={"id": 1}),
            {
                "name": "SYLVER",
                "price": "9.0",
            },
            content_type="application/json",
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_subscribe_status(self):
        data = {"is_active": True}
        response = self.client.put(
            reverse("update_subscribe_status", kwargs={"id": 1}),
            data=json.dumps(data),
            content_type="application/json",
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class SponsorCOdeTest(TestCase):
    def test_url_sponsor_code(self):

        response = self.client.post(
            reverse("check_sponsor_code"),
            {"code": "Admin123!"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)


class activationTest(TestCase):
    def test_activate_phone(self):

        r = Reward.objects.create(sum="11.0") 

        u = Client.objects.create(
            firstname="MIIJ",
            email="mchristian@hairun-technology.com",
            password="Admin123!!!",
            # is_super_admin = True,
            phone="+261340061032",
            reward=r,
        )

        u.phone_is_activated = True

        u.save()

    def test_activate_account(self):

        r = Reward.objects.create(sum="11.0")

        u = Client.objects.create(
            firstname="MIIJ",
            email="mchristian@hairun-technology.com",
            password="Admin123!!!",
            # is_super_admin = True,
            phone="+261340161032",
            reward=r,
        )

        u.account_is_active = True

        u.save()


class TestReward(TestCase):
    
    def test_update_reward_credit(self):

        response = self.client.patch(
            reverse("update_reward_credit", kwargs={"id": 1}),
            {"sum": "10.00"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_reward_free_day_(self):

        response = self.client.patch(
            reverse("update_reward_day", kwargs={"id": 1}),
            {"free_day": "20"},
            content_type="application/json",
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_credit_user(self):

        response = self.client.patch(
            reverse("update_reward_credit", kwargs={"id": 2}),
            {"sum": "10.00"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCodereduction(TestCase):
    def setUp(self):

        self.valid_data = {
            "code_name": "DIAMOND",
            "code": "A244M",
            "reduction": "10.0",
            "client_is_subscribed": True,
            "expiry": "2022-10-10 19:38:21.363070",
            "clients": "1",
            "subscribes": "1",
        }

    def test_add_reduction_code(self):
        response = self.client.post(
            reverse("create_reduction_code"),
            data=json.dumps(self.valid_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_update_reduction_code(self):
        data = {
          
            "code_name":"SYLVER",
            "code": "A244M",
            "reduction":"18.0",
            "client_is_subscribed": True,
            "expiry":  "2023-10-10 19:38:21.363070",
            "clients": "1", 
            "subscribes": "1" 
        }
        response = self.client.patch(
            reverse('update_reduction_code', kwargs={'id': 1}),   
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)   
        


    def test_delete_code(self):
        response = self.client.delete(reverse("delete_code", kwargs={"id": 1}))
        ##self.assertEqual(response.status_code, status.HTTP_200_OK)dd
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_display_reduction_code(self):
        # get API response
        response = self.client.get(reverse("get_all_reduction_code"))
        # get data from db
        experiments = CodeReductionAvailable.objects.all()
        serializer = CodeReductionAvailableSerializer(experiments, many=True)  
        #self.assertEqual(response.data, serializer.data) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)            
 

class CreatePaire(APITestCase):
    def test_url_(self):

        response = self.client.get(reverse("get_all_couple_demand"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    ###LOAD couple
    def test_url_load_data(self): 

        response = self.client.get(reverse("load_couple_data"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def setUp(self):

        self.data = {
            "symbol_1": "USD",
            "symbol_1_logo": "euro.png",
            "symbol_2": "ETH",
            "symbol_2_logo": "euro.png",
            "intervals": "1h",
        }

    def test_create_couple(self):
        response = self.client.post(
            reverse("create_couple"),
            data=json.dumps(self.data),
            content_type="application/json",
        )
        ### self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_couple(self):
        data = {
            "symbol_1": "BTC",
            "symbol_1_logo": "euro.png",
            "symbol_2": "ETH",
            "symbol_2_logo": "euro.png",
        }
        response = self.client.patch(
            reverse("update_couple_info", kwargs={"id": 1}),
            data=json.dumps(self.data),
            content_type="application/json",
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testgetAllCouple(self):
        # id = jwt.decode(1, os.environ.get("SECRET_KEY"), algorithms="HS256")["id"]
        # response = self.client.get( reverse("get_all_couple", kwargs = {'pk': id}))
        couple = Couple.objects.create(
            symbol_1="BTC",
            symbol_2="USD",
            symbol_1_logo="LOGO",
            symbol_2_logo="LOGO",
            created_at=datetime.now(),
        )

        # response = self.client.get( reverse("get_all_couple", kwargs = {'pk': 1}))
        """
        couple_id = Couple.objects.get(symbol_1='BTC').id
        response = self.client.get(reverse('get_all_couple', args=(couple_id,))) 
        self.assertEqual(response.status_code, 200)   
        """

    # test that detail page returns a 404 if the item does not exist.


class TestTicketEndPoint(APITestCase):
    pk = "1"
    url = reverse("get_all_tickets")
    url_ticket = reverse("create_ticket")

    def test_url_ticket(self):

        response = self.client.get(reverse("get_all_tickets"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def setUp(self):
        r = Reward.objects.create(sum="10.0")

        customers = Client.objects.create(
            firstname="MIJARIMANANA",
            email="ds@hairun-technology.com",
            password="Azerty123!",
            phone="+261341261032",
            reward=r,
        )

        Ticket.objects.create(
            client=customers, name="TicketsWIP", created_at=datetime.utcnow()
        )

    def testgetTicket(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    """
    def testgetClientTicket(self): 
        
        r = Reward.objects.create(sum = '10.0')
        
        u = Client.objects.create(       
                firstname = 'MIIJ', 
                email = 'mchristian@hairun2-technology.com',  
                password = 'Admin123!!!',
                #is_super_admin = True,  
                phone = '+261341461032',   
                reward=r   
                )       
        #u.is_active = False 
        
        u.email_is_activated = True  
        
        u.phone_is_activated = True 
        u.account_is_active = True 
        u.save() 
        #payload = jwt_payload_handler(u.id)            
        #token = jwt_encode_handler(payload)            

        id = jwt.decode(ClientToken, os.environ.get("SECRET_KEY"), algorithms="HS256")["id"]
       # self.client.credentials(Authorization='JWT {0}'.format(token))
        response = self.client.get(reverse('get_client_tickets',kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
    """

    def testcreateTicket(self):

        r = Reward.objects.create(sum="10.0")

        customers = Client.objects.create(
            firstname="MIJARIMANANA",
            email="fahitriniaina@hairun-technology.com",
            password="Azerty123!",
            phone="+261342261039",
            reward=r,
        )
        data = {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNjM2NTcxODIzLCJpYXQiOjE2MzY1Mjg2MjN9.eyp7vYUR49TDvP6_VSKoLlpFvox_D2rq6tHtm77sxP0",
            "client": customers,
            "name": "HAIRUN",
            "created_at": datetime.utcnow(),
        }
        response = self.client.post(self.url_ticket, data=data)
        self.assertEqual(response.status_code, 401)

    def updateTiecketStatus(self):

        id = "1"
        data = {"status": False}
        response = self.client.patch(
            reverse("update_ticket_status" + f"/{id}"), data=data
        )

        self.assertEqual(response.status_code, 200)

    def testfunction(self):
        return "PIRNT"

    def testCreateTicketMessage(self):
        id = "1"
        r = Reward.objects.create(sum="10.0")

        customers = Client.objects.create(
            firstname="MIJARIMANANA",
            email="Christiands@hairun-technology.com",
            password="Azerty123!",
            phone="+261343361032",
            reward=r,
        )

        ticket = Ticket.objects.create(
            client=customers, name="TicketsWIP", created_at=datetime.utcnow()
        )

        data = {"created_at": datetime.utcnow(), "date_message": datetime.utcnow()}
        response = self.client.post(
            reverse("create_ticket_message", kwargs={"id": 1}), data=data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 

