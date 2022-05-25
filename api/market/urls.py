from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import static
from django.conf import settings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register("users", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/", include("predict.urls")),
    path("api/", include("prediction.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
