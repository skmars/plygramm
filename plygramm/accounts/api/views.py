from rest_framework import serializers
from rest_framework.views import APIView

from plygramm.accounts.models import Account
from plygramm.accounts.selectors import get_account_list
from plygramm.api.services.pagination import LimitOffsetPagination, get_paginated_response


# TODO: When JWT is resolved, add authenticated version
class AccountListAPI(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        email = serializers.EmailField()
        role = serializers.CharField()
        is_active = serializers.BooleanField(required=False, allow_null=True)  # default=None

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Account
            fields = ("id", "email", "role", "is_active")

    def get(self, request):
        # Filters validation, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        accounts = get_account_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=accounts,
            request=request,
            view=self,
        )
