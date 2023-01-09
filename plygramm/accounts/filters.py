import django_filters

from plygramm.accounts.models import Account


class AccountFilter(django_filters.FilterSet):
    class Meta:
        model = Account
        fields = (
            "id",
            "email",
            "role",
            "is_active",
        )
