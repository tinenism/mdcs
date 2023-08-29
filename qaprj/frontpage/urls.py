from django.urls import path
from .views import AccountRegisterView
from . import views

urlpatterns = [
    path('', views.front, name='frontpage'),
    path('signup/', AccountRegisterView.as_view(), name='signup'),
    
    # path('acccounts/login', AccountLoginView.as_view(), name='login')
]
