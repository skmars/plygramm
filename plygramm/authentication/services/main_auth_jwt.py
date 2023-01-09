import uuid

from plygramm.accounts.models import Account


def auth_account_get_jwt_secret_key(account: Account) -> str:
    return str(account.jwt_key)


def auth_jwt_response_payload_handler(token, account=None, request=None, issued_at=None):
    response = {"token": token}
    if account is not None:
        return response.update(
            {
                "account_id": account.id,
                "account_role": account.role,
                "is_active": account.is_active,
                "date_joined": account.date_joined,
            }
        )

    return response


def jwt_auth_logout(account: Account) -> Account:
    account.jwt_key = uuid.uuid4()
    account.full_clean()
    account.save(update_fields=["jwt_key"])

    return account
