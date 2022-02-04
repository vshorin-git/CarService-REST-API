from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import *


class ClientProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientProfileDetailSerializer
    queryset = ClientProfile.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class MasterProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MasterProfileDetailSerializer
    queryset = MasterProfile.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentDetailSerializer
    queryset = Appointment.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)


class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentListSerializer
    queryset = Appointment.objects.all()
    ordering = ('date')
    permission_classes = (IsAdminUser,)


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentDetailSerializer
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated,)
