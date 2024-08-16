from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserViewSet, PaymentCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"", UserViewSet, basename="users")
user_create = UserViewSet.as_view({"post": "create"})
user_detail = UserViewSet.as_view({"get": "retrieve"})
user_update = UserViewSet.as_view({"put": "update", "patch": "partial_update"})
user_delete = UserViewSet.as_view({"delete": "destroy"})


urlpatterns = (
    format_suffix_patterns(
        [
            path("register/", user_create, name="register"),
            path("detail/<int:pk>/", user_detail, name="user-detail"),
            path("update/<int:pk>/", user_update, name="user-detail"),
            path("delete/<int:pk>/", user_delete, name="user-delete"),
            path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
            path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
            path(
                "token/",
                TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
                name="token",
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
