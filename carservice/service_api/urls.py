from django.urls import path

from . import views

urlpatterns = [
    path('client/<str:pk>/', views.ClientProfileDetailView.as_view()),
    path('master/<str:pk>/', views.MasterProfileDetailView.as_view()),
    path('appointment/all', views.AppointmentListView.as_view()),
    path('appointment/create', views.AppointmentCreateView.as_view()),
    path('appointment/<int:pk>', views.AppointmentDetailView.as_view()),
]
