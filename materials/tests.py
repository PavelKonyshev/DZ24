from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="apitest@apitest.com")
        self.course = Course.objects.create(
            title="Test Course", description="Test Course", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="Test Lesson",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.course.title)

    def test_course_create(self):
        url = reverse("materials:course-list")
        data = {
            "title": "Test Course 2",
            "description": "Test Course 2",
            "owner": self.user.pk,
        }
        response = self.client.post(url, data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {
            "title": "Test Course",
        }
        response = self.client.get(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test Course")

    def test_course_delete(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        url = reverse("materials:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="apitest@apitest.com")
        self.course = Course.objects.create(
            title="Test Course", description="Test Course", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="Test Lesson",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        # url = reverse("materials:lesson_list")
        data = {
            "title": "Test Lesson 2",
            "description": "Test Lesson 2",
            "course": self.course.pk,
            "owner": self.user.pk,
        }
        response = self.client.post("/lesson/create/", data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        data = {
            "title": "Test Lesson",
        }
        response = self.client.get(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test Lesson")

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        response = self.client.get("/lesson/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="apitest@apitest.com")
        self.course = Course.objects.create(
            title="Test Course", description="Test Course"
        )
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        Subscription.objects.all().delete()
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.post("/subscription/create/", data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.all()[0].course, self.course)

    def test_subscription_list(self):
        response = self.client.get("/subscription/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
