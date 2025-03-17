from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any

from apt_get_trade.application.account.services import AccountService

router = APIRouter(prefix="/account", tags=["account"])


def get_account_service():
    """AccountService 의존성 주입"""
    return AccountService()


@router.get("/token")
def get_access_token(service: AccountService = Depends(get_account_service)):
    """접근 토큰 발급"""
    try:
        token = service.get_access_token()
        return {"access_token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/overseas/balance")
def get_overseas_balance(
    exchange_code: str = "NASD",
    currency: str = "USD",
    service: AccountService = Depends(get_account_service)
):
    """해외주식 잔고 조회"""
    try:
        balance = service.get_overseas_balance(exchange_code, currency)
        return balance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/overseas/account")
def get_overseas_account(
    exchange_code: str = "NASD",
    service: AccountService = Depends(get_account_service)
):
    """해외주식 계좌 조회"""
    try:
        account = service.get_overseas_account(exchange_code)
        return account
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/overseas/info")
def get_account_info(
    exchange_code: str = "NASD",
    service: AccountService = Depends(get_account_service)
):
    """해외주식 계좌 정보 조회 (도메인 객체)"""
    try:
        account_info = service.get_account_info(exchange_code)
        return {
            "account_number": account_info.account_number,
            "product_code": account_info.product_code,
            "currency": account_info.currency,
            "cash_balance": account_info.cash_balance,
            "total_balance": account_info.total_balance,
            "total_purchase_amount": account_info.total_purchase_amount,
            "total_evaluation_amount": account_info.total_evaluation_amount,
            "total_profit_loss": account_info.total_profit_loss,
            "total_profit_loss_rate": account_info.total_profit_loss_rate,
            "stocks": [
                {
                    "symbol": stock.symbol,
                    "name": stock.name,
                    "quantity": stock.quantity,
                    "avg_price": stock.avg_price,
                    "current_price": stock.current_price,
                    "total_value": stock.total_value,
                    "profit_loss": stock.profit_loss,
                    "profit_loss_rate": stock.profit_loss_rate
                }
                for stock in account_info.stocks
            ] if account_info.stocks else []
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 