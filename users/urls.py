from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"", UserViewSet, basename="users")
user_create = UserViewSet.as_view({"post": "create"})


urlpatterns = (
    format_suffix_patterns(
        [
            path("register/", user_create, name="register"),
            path(
                "login/",
                TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
                name="login",
            ),
            path(
                "token/refresh/",
                TokenRefreshView.as_view(permission_classes=(AllowAny,)),
                name="token_refresh",
            ),
        ]
    )
    + router.urls
)
