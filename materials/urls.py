from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonDestroyApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    SubscriptionCreateApiView,
    SubscriptionListApiView,
)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_detail"),
    path(
        "lesson/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"
    ),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"
    ),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path(
        "subscription/create/",
        SubscriptionCreateApiView.as_view(),
        name="subscription_create",
    ),
    path("subscription/", SubscriptionListApiView.as_view(), name="subscription_list"),
] + router.urls

urlpatterns += router.urls
