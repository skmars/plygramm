from django.db.models.query import QuerySet

from plygramm.accounts.filters import AccountFilter
from plygramm.accounts.models import Account


def get_account_login_data(*args, account: Account):
    return {
        "id": account.id,  # type:ignore
        "email": account.email,
        "role": account.role,
        "is_active": account.is_active,
        "is_superuser": account.is_superuser,
    }


def get_account_list(*args, filters=None) -> QuerySet[Account]:
    filters = filters or {}

    account_qs = Account.objects.all()

    return AccountFilter(filters, account_qs).account_qs  # type:ignore
