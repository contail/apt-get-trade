from fastapi import APIRouter
from apt_get_trade.interfaces.api.account_api import router as account_router

api_router = APIRouter()
api_router.include_router(account_router) 