from sqlalchemy.orm import Session
from apps.accounts.models import Account

def create_account(db: Session, account_data: dict) -> Account:
    """
    Create a new account in the database.
    """
    account = Account(**account_data)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def get_account_by_id(db: Session, account_id: str) -> Account | None:
    """
    Retrieve an account by its ID.
    Returns None if not found.
    """
    return db.query(Account).filter(Account.id == account_id).first()

def get_all_accounts(db: Session) -> list[Account]:
    """
    Retrieve all accounts from the database.
    """
    return db.query(Account).all()

def get_account_by_username(db: Session, username: str) -> Account | None:
    """
    Retrieve an account by username.
    """
    return db.query(Account).filter(Account.username == username).first()

def delete_account(db: Session, account_id: str) -> bool:
    """
    Delete an account by its ID.
    Returns True if deleted, False if not found.
    """
    account = get_account_by_id(db, account_id)
    if account:
        db.delete(account)
        db.commit()
        return True
    return False
