from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from setup import get_db
from apps.accounts.schemas import AccountCreate, AccountResponse
from apps.accounts.views_manager import create_account_view, get_account_view

router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account_view(account, db)

@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: str, db: Session = Depends(get_db)):
    return get_account_view(account_id, db)
