from django.urls import path

from .views import index, RegistrationView

urlpatterns = [
    path('', index, name='index'),
    path('registration/', RegistrationView.as_view(), name='registration')
]
