from typing import Optional

from django.db import transaction

from plygramm.accounts.models import Account
from plygramm.common.services.model_update import model_update

"""
Here we using functional-based views for api
"""


def user_create(
    *args,
    email: str,
    role: str,
    password: str,
    nickname: Optional[str] = None,
    controll_question: Optional[str] = None,
    answer_controll_question: Optional[str] = None,
    is_active: bool = True,
) -> Account:
    user = Account.objects.create_user(
        email=email,
        password=password,
        role=role,
        nickname=nickname,
        controll_question=controll_question,
        answer_controll_question=answer_controll_question,
        is_active=is_active,  # type: ignore
    )

    return user


@transaction.atomic
def user_update(*args, account: Account, data) -> Account:
    non_side_effect_fields = [
        "nickname",
    ]

    account, has_updated = model_update(instance=account, fields=non_side_effect_fields, data=data)
    return account
