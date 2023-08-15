from rest_framework import serializers
from authentication.serializers import ProfileSerializer
from .models import Field, Plato, Lesson, Schedule
from django.db.models import Q


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
    field = FieldSerializer()

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'code', 'field',
                  'theory_course', 'practical_course')


class CreateScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'start_time', 'end_time', 'date_of_week',
                  'plato', 'lesson', 'professor', 'capacity', 'exam_name',
                  'exam_date', 'exam_start_time', 'exam_end_time', 'exam_location',)

    def validate(self, attrs):
        super().validate(attrs)
        schedule_list = Schedule.objects.filter(Q(date_of_week=attrs['date_of_week']) & Q(
            start_time__lt=attrs['end_time']) & Q(end_time__gt=attrs['start_time'])).all()
        error_list = []
        for schedule in schedule_list:
            if schedule.professor == attrs['professor']:
                error_list.append('professor is not available')
            if schedule.plato == attrs['plato']:
                error_list.append('plato is not available')
        if len(error_list) > 0:
            raise serializers.ValidationError(dict(schedule_error=error_list))
        return super().validate(attrs)


class ListScheduleSerializer(serializers.ModelSerializer):
    plato = PLatoSerializer()
    professor = ProfileSerializer()
    lesson = ListLessonSerializer()

    class Meta:
        model = Schedule
        fields = ('id', 'start_time', 'end_time', 'date_of_week',
                  'plato', 'lesson', 'professor', 'capacity',)
