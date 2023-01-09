import datetime

from config.env import env

# More settings from here - https://styria-digital.github.io/django-rest-framework-jwt/#additional-settings

# Default to 7 days
JWT_EXPIRATION_DELTA_SECONDS = env("JWT_EXPIRATION_DELTA_SECONDS", default=60 * 60 * 24 * 7)  # type: ignore
JWT_AUTH_COOKIE = env("JWT_AUTH_COOKIE", default="jwt")  # type: ignore
JWT_AUTH_COOKIE_SAMESITE = env("JWT_AUTH_COOKIE_SAMESITE", default="Lax")  # type: ignore
JWT_AUTH_HEADER_PREFIX = env("JWT_AUTH_HEADER_PREFIX", default="Bearer")  # type: ignore


JWT_AUTH = {
    "JWT_GET_USER_SECRET_KEY": "plygramm.authentication\
                                    .services\
                                        .main_auth_jwt\
                                            .auth_account_get_jwt_secret_key",
    "JWT_RESPONSE_PAYLOAD_HANDLER": "styleguide_example\
                                        .authentication\
                                            .services\
                                                .main_auth_jwt\
                                                    .auth_jwt_response_payload_handler",
    "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=JWT_EXPIRATION_DELTA_SECONDS),
    "JWT_ALLOW_REFRESH": False,
    "JWT_AUTH_COOKIE": JWT_AUTH_COOKIE,
    "JWT_AUTH_COOKIE_SECURE": True,
    "JWT_AUTH_COOKIE_SAMESITE": JWT_AUTH_COOKIE_SAMESITE,
    "JWT_AUTH_HEADER_PREFIX": JWT_AUTH_HEADER_PREFIX,
}
