from fastapi import HTTPException
from sqlalchemy.orm import Session
from apps.accounts.schemas import AccountCreate, AccountResponse
from apps.accounts.views import create_account, get_account_by_id
import json

def create_account_view(account: AccountCreate, db: Session) -> AccountResponse:
    try:
        return create_account(db, json.loads(account.model_dump_json()))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_account_view(account_id: str, db: Session) -> AccountResponse:
    account = get_account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

