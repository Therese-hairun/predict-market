from os import name
from django.urls import path

from . import views


urlpatterns = [
    ######################################################### GESTION CLIENT ###################################################
    # LIST
    path("user_list", views.ApiSubscriptionListView.as_view(), name="user_list"),
    path("user", views.get_user_by_token, name="customer_by_id"),
    path("user_list/<id>", views.get_user_by_id, name="customer_list_by_id"),
    path("client", views.get_client, name="get_client"),
    # CREATE
    path("create_client", views.create_client, name="create_client"),
    # UPDATE
    path("updatePassword", views.update_password, name="update_password"),
    path("account_status/<id>", views.change_cusomer_status, name="account_status"),
    path("activate_phone", views.update_phone_status, name="activate_phone"),
    path("activate_email", views.update_email_status, name="activate_email"),
    path(
        "update_client_infos",
        views.update_client_general_info,
        name="update_client_infos",
    ),
    path("update_phone", views.update_phone, name="update_phone"),
    path(
        "update_client_subscribe/<id>",
        views.update_client_subscribe,
        name="update_client_subscribe",
    ),
    path("upload_user_profil", views.upload_user_profil, name="upload_user_profil"),
    path(
        "update_renew_status",
        views.renew_subscription_status,
        name="update_renew_status",
    ),
    # LOGIN
    path("login", views.login, name="login"),
    # SEND SMS AND MAIL
    path("sendMail", views.send_mail, name="send_mail"),
    path("sendSMS", views.send_sms, name="send_sms"),
    # RESET PASSWORD
    path("resetPassword", views.reset_password, name="reset_password"),
    # PHONE
    path("verify_phone", views.verify_phone, name="verify_phone"),
    path("phone_used", views.is_phone_used, name="is_phone_used"),
    # ACCOUNT STATUS
    path("verify_account", views.verify_account, name="verify_account"),
    ######################################################### GESTION SUBSCRIBE ###################################################
    # LIST
    path("subscribe", views.ApiSubscribeListView.as_view(), name="get_subcribe"),
    path("subscribe/<id>", views.get_by_subscribe_id, name="get_subcribe_by_id"),
    path(
        "upgrade_subscribe/<id>",
        views.ApiUpgradeSubscribeListView.as_view(),
        name="get_upgrade_subcribe",
    ),
    # CREATE
    path("add_subscribe", views.add_subscribe, name="add_subscribe"),
    # UPDATE
    path("updateSubscribe/<id>", views.update_subscribe, name="update_subscribe"),
    path(
        "updateSubscribeStatus/<id>",
        views.update_subscribe_status,
        name="update_subscribe_status",
    ),
    path(
        "recommanded_subscribe/<id>",
        views.update_subscribe_recommanded,
        name="recommanded_subscribe",
    ),
    ######################################################### GESTION ADMIN ###################################################
    # LIST
    path("admin", views.get_admin, name="get_admin"),
    # CREATE
    path("create_admin", views.create_admin, name="create_admin"),
    ######################################################### GESTION REDUCTION CODE ###################################################
    # LIST
    path(
        "reduction_code",
        views.ApiReductionCodeListView.as_view(),
        name="get_all_reduction_code",
    ),
    # CREATE
    path(
        "create_reduction_code",
        views.create_reduction_code,
        name="create_reduction_code",
    ),
    # UPDATE
    path("update_code/<id>", views.update_reduction_code, name="update_reduction_code"),
    # DELETE
    path("delete_code/<id>", views.delete_reduction_code, name="delete_code"),
    # CHECK
    path("use_reduction", views.use_reduction_code, name="use_reduction_code"),
    ######################################################### GESTION CLIENT REWARD ###################################################
    # LIST
    path("reward", views.ApiRewardListView.as_view(), name="get_reward"),
    path("reward/<id>", views.get_reward_by_id, name="get_reward_by_id"),
    # UPDATE
    path("updateClient_credit/<id>", views.update_reward, name="update_reward_credit"),
    path(
        "updateClient_free_day/<id>",
        views.update_reward_free_day,
        name="update_reward_day",
    ),
    ######################################################### GESTION SUBSCRIPTION ###################################################
    # UPDATE
    path("add_days", views.add_days_to_subscription, name="add_days_to_subscription"),
    path(
        "add_credits",
        views.add_credit_to_subscription,
        name="add_credits_to_subscription",
    ),
    # CHECK
    path(
        "check_subscription",
        views.check_subscription,
        name="check_subscription_expiry",
    ),
    ######################################################### GESTION PAYMENT AND INVOICE ###################################################
    path("payement", views.payement, name="payement"),
    path("prorata", views.prorata, name="prorata_value"),
    path(
        "remove_couple_downgrade",
        views.remove_couple_for_downgrade,
        name="remove_couple_for_downgrade",
    ),
    path("invoice", views.ApiInvoiceListView.as_view(), name="get_all_invoice"),
    ######################################################### GESTION DEMAND COUPLE ###################################################
    # LIST
    path(
        "get_all_couple_demand",
        views.ApiCoupleDemandeListView.as_view(),
        name="get_all_couple_demand",
    ),
    # CREATE
    path(
        "create_demande_couple",
        views.create_demande_couple,
        name="create_demande_couple",
    ),
    # UPDATE
    path(
        "validate_demand/<symbol1>/<symbol2>",
        views.validate_demande,
        name="validate_couple_demand",
    ),
    ######################################################### GESTION COUPLE ###################################################
    # LIST
    path("couple", views.ApiCoupleListView.as_view(), name="get_couple"),
    path(
        "couple/<symbol1>/<symbol2>",
        views.get_couple_by_symbol,
        name="get_couple_by_symbol",
    ),
        path(
        "couple_user/<symbol1>/<symbol2>",
        views.get_couple_user,
        name="get_couple_user",
    ),
    path("couples", views.get_all_couple, name="get_all_couple"),
    path(
        "couple_data/<symbol>", views.get_couple_data, name="get_couple_data"
    ),
        path(
        "prediction/<symbol>", views.get_couple_prediction, name="get_couple_prediction"
    ),
    path("moment_couple", views.get_moment_couple, name="get_moment_couple"),
    path("explosive_couple", views.get_explosive_couple, name="get_explosive_couple"),
    path("client_couple", views.get_client_couple, name="get_client_couple"),
    path(
        "couple_client/<id>",
        views.get_couple_client,
        name="get_couple_client_by_client_id",
    ),
    path("load_couple", views.load_couple_data, name="load_couple_data"),
    # CREATE
    path("create_couple", views.create_couple, name="create_couple"),
    # UPDATE
    path(
        "updateCoupleStatus/<id>",
        views.update_couple_status,
        name="update_couple_status",
    ),
    path(
        "updateCoupleInfo/<id>",
        views.update_couple_info,
        name="update_couple_info",
    ),
    # DELETE
    path(
        "delete_couple/<id>",
        views.delete_couple,
        name="delete_couple",
    ),
    ######################################################### GESTION FAVORITE COUPLE ###################################################
    # LIST
    path(
        "favorite_couple",
        views.get_client_favorite_couple,
        name="get_client_favorite_couple",
    ),
    # CREATE
    path(
        "create_favorite_couple",
        views.create_favorite_couple,
        name="create_favorite_couple",
    ),
    # DELETE
    path(
        "delete_favorite_couple/<symbol1>/<symbol2>",
        views.delete_favorite_couple,
        name="delete_favorite_couple",
    ),
    ######################################################### GESTION COUPLE VISUALIZATION ###################################################
    path(
        "add_couple_visualisation",
        views.add_couple_for_visualisation,
        name="add_couple_for_visualisation",
    ),
    path(
        "remove_couple_visualisation",
        views.remove_couple_for_visualisation,
        name="remove_couple_for_visualisation",
    ),
    path(
        "visualize/<symbol1>/<symbol2>", views.visualize_couple, name="visualize_couple"
    ),
    ######################################################### GESTION TICKET ###################################################
    # LIST
    path("tickets_list", views.ApiTicketListView.as_view(), name="get_all_tickets"),
    path(
        "tickets",
        views.ApiClientTicketListView.as_view(),
        name="get_client_tickets",
    ),
    path("ticket/<id>", views.ticket_details, name="get_ticket_details"),
    path(
        "admin_ticket/<id>",
        views.admin_ticket_details,
        name="get_ticket_details_for_admin",
    ),
    # CREATE
    path("create_ticket", views.create_ticket, name="create_ticket"),
    # UPDATE
    path(
        "update_ticket_status/<id>",
        views.update_ticket_status,
        name="update_ticket_status",
    ),
    path(
        "update_admin_ticket_status/<id>",
        views.update_admin_ticket_status,
        name="update_admin_ticket_status",
    ),
    ######################################################### GESTION TICKET MESSAGE ###################################################
    # LIST
    # CREATE
    path(
        "create_ticket_message/<id>",
        views.create_ticket_message,
        name="create_ticket_message",
    ),
    path(
        "create_admin_ticket_message/<id>",
        views.create_admin_ticket_message,
        name="create_admin_ticket_message",
    ),
    ######################################################### GESTION PARRAINAGE ###################################################
    # LIST
    path(
        "client_filleul/<str:code>",
        views.ApiClientFilleulListView.as_view(),
        name="get_client_filleul",
    ),
    # CODE
    path("check_code", views.verify_sponsor_code, name="check_sponsor_code"),
    ######################################################### OTHER ###################################################
    path(
        "change_couple_validation_state/<id>",
        views.change_validated_status,
        name="change_couple_validation_state",
    ),
    path("check_downgrade", views.check_downgrade, name="check_downgrade"),
    path("share_linkedin", views.share_linkedin, name="share_linkedin"),
    ######################################################### API LOGS ###############################################################
    path(
        "api_log",
        views.ApiLogsList.as_view(),
        name="api_log",
    ),
    ######################################################### TOKEN AND PASSWORD ###################################################
    path("verify_token", views.verify_token, name="verify_token"),
    path("verify_password", views.verify_password, name="verify_password"),
    path("generate_token", views.generateAuthToken, name="generate_token"),
]
