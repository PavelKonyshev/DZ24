from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDatailSerializer(ModelSerializer):
    course_count = SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_course_count(self, cont):
        return Lesson.objects.filter(course=cont).count()




class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
