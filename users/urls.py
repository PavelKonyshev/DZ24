from django.urls import path
from materials.views import CourseViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from users.apps import UsersConfig
from users.views import PaymentListAPIView
from rest_framework.routers import DefaultRouter

app_name = UsersConfig.name

router = DefaultRouter()
router.register("", CourseViewSet)


urlpatterns = (
    format_suffix_patterns(
        [
            path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
        ]
    )
    + router.urls
)
