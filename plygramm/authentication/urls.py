from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import LogInView, LogOutView

app_name = "users"

urlpatterns = [
    path("log_in/", LogInView.as_view(), name="log_in"),
    path("log_out/", LogOutView.as_view(next_page="log_in"), name="log_out"),
]
