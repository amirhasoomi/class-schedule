from rest_framework import serializers
from authentication.serializers import ProfileSerializer
from .models import Field, Plato, Lesson, Exam, Schedule


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('pk', 'name', 'code',)


class PLatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = ('id', 'name', 'building', 'capacity',)


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'code', 'field',
                  'theory_course', 'practical_course')


class ListLessonSerializer(serializers.ModelSerializer):
    # field = FieldSerializer()

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'code', 'field',
                  'theory_course', 'practical_course')


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'name', 'date', 'start_time', 'end_time', 'location',)


class CreateScheduleSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()

    class Meta:
        model = Schedule
        fields = ('id', 'start_time', 'end_time', 'date_of_week',
                  'plato', 'lesson', 'professor', 'capacity', 'exam',)

    def validate(self, attrs):

        return super().validate(attrs)


class ListScheduleSerializer(serializers.ModelSerializer):
    plato = PLatoSerializer()
    professor = ProfileSerializer()
    exam = ExamSerializer()

    class Meta:
        model = Schedule
        fields = ('id', 'start_time', 'end_time', 'date_of_week',
                  'plato', 'lesson', 'professor', 'capacity', 'exam',)
