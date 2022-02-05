from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import datetime, timezone

from .models import *

User = get_user_model()


class ClientProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ClientProfile
        fields = ('user', 'first_name', 'last_name', 'patronymic', 'car_brand', 'car_model')


class MasterProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MasterProfile
        fields = '__all__'


class AppointmentListSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    master = serializers.StringRelatedField()

    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('date', 'master')

    def validate(self, data):
        """
        Проверка доступности даты для записи.
        """
        client = ClientProfile.objects.get(user=self.context['request'].user)
        data.update({'client': client})
        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()  # local time
        if Appointment.objects.filter(date=data['date']):
            raise serializers.ValidationError("Выбранная дата уже занята, пожалуйста, выберите другую дату")
        elif data['date'] <= dt:
            raise serializers.ValidationError("Указана дата в прошлом, пожалуйста, выберите другую")
        return data
