from django.urls import include, path

from .views import (
    AccountJwtLoginApi,
    AccountJwtLogoutApi,
    AccountSessionLoginApi,
    AccountSessionLogoutApi,
)

urlpatterns = [
    path(
        "session/",
        include(
            (
                [
                    path("log_in/", AccountSessionLoginApi.as_view(), name="login"),
                    path("log_out/", AccountSessionLogoutApi.as_view(), name="logout"),
                ],
                "session",
            )
        ),
    ),
    path(
        "jwt/",
        include(
            (
                [
                    path("login/", AccountJwtLoginApi.as_view(), name="login"),
                    path("logout/", AccountJwtLogoutApi.as_view(), name="logout"),
                ],
                "jwt",
            )
        ),
    ),
]
