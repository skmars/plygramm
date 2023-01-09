from django.urls import path

from .views import AccountListAPI

urlpatterns = [path("accounts/", AccountListAPI.as_view(), name="list_of_accounts")]
