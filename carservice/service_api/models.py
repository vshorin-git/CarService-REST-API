from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    car_brand = models.CharField(max_length=50, verbose_name='Марка автомобиля')
    car_model = models.CharField(max_length=50, verbose_name='Модель автомобиля')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MasterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    SPECIALITIES = (
        (1, 'Моторист'),
        (2, 'Автоэлектрик'),
        (3, 'Маляр'),
        (4, 'Вулканизаторщик'),
        (5, 'Автожестянщик'),
        (6, 'Механик-диагност'),
    )
    speciality = models.IntegerField(verbose_name='Специализация', choices=SPECIALITIES, max_length=1)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.get_speciality_display()}'


class Appointment(models.Model):
    date = models.DateTimeField(verbose_name='Дата и время записи')
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, verbose_name='Клиент')
    master = models.ForeignKey(MasterProfile, on_delete=models.CASCADE, verbose_name='Мастер')

    def __str__(self):
        return f'{self.client} - {self.master} - {self.date}'
