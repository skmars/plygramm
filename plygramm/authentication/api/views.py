from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebTokenView

from plygramm.accounts.selectors import get_account_login_data
from plygramm.api.services.session_auth_mixin import ApiAuthMixin
from plygramm.authentication.services.main_auth_jwt import jwt_auth_logout


class AccountSessionLoginApi(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()
        role = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = authenticate(request, **serializer.validated_data)  # type: ignore

        if account is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        login(request, account)

        data = get_account_login_data(account=account)
        session_key = request.session.session_key

        return Response({"session": session_key, "data": data})


class AccountSessionLogoutApi(APIView):
    def get(self, request):
        logout(request)

        return Response()

    def post(self, request):
        logout(request)

        return Response()


class AccountJwtLoginApi(ObtainJSONWebTokenView):
    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            response.status_code = status.HTTP_200_OK

        return response


class AccountJwtLogoutApi(ApiAuthMixin, APIView):
    def post(self, request):
        jwt_auth_logout(request.account)

        response = Response()

        if settings.JWT_AUTH["JWT_AUTH_COOKIE"] is not None:
            response.delete_cookie(settings.JWT_AUTH["JWT_AUTH_COOKIE"])

        return response
