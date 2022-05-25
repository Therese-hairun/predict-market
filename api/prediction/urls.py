from django.urls.conf import path
from . import views

urlpatterns = [
    path("assets", views.ApiAssetListView.as_view(), name="asset_list"),
    path("symbols", views.ApiSymbolListView.as_view(), name="symbol_list"),
    path("training/<symbol>", views.get_training, name="training_list"),
]
