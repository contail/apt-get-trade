from typing import Dict, Any, List

from apt_get_trade.core.config import ACCOUNT_NO, PRODUCT_CODE
from apt_get_trade.domain.account.models import AccountInfo, Balance
from apt_get_trade.infrastructure.external_services.korea_investment_api import KoreaInvestmentAPI


class AccountService:
    """계좌 관련 서비스"""
    
    def __init__(self):
        self.api_client = KoreaInvestmentAPI()
        self.account_no = ACCOUNT_NO
        self.product_code = PRODUCT_CODE
    
    def get_access_token(self) -> str:
        """접근 토큰 발급"""
        return self.api_client.get_access_token()
    
    def get_overseas_balance(self, exchange_code: str = 'NASD', currency: str = 'USD') -> Dict[str, Any]:
        """해외주식 잔고 조회 (원본 API 응답)"""
        return self.api_client.get_overseas_balance(
            self.account_no, 
            self.product_code, 
            exchange_code, 
            currency
        )
    
    def get_overseas_account(self, exchange_code: str = 'NASD') -> Dict[str, Any]:
        """해외주식 계좌 조회 (원본 API 응답)"""
        return self.api_client.get_overseas_account(
            self.account_no, 
            self.product_code, 
            exchange_code
        )
    
    def get_account_info(self, exchange_code: str = 'NASD') -> AccountInfo:
        """해외주식 계좌 정보 조회 (도메인 객체)"""
        # 계좌 정보 조회
        account_data = self.get_overseas_account(exchange_code)
        
        # 도메인 객체로 변환
        account_info = AccountInfo.from_api_response(
            account_data, 
            self.account_no, 
            self.product_code
        )
        
        # 잔고 정보 조회
        balance_data = self.get_overseas_balance(exchange_code)
        
        # 보유 주식 정보 추출 및 변환
        stocks = []
        if 'output1' in balance_data:
            for item in balance_data.get('output1', []):
                stock = Balance(
                    currency=item.get('tr_crcy_cd', 'USD'),
                    symbol=item.get('ovrs_pdno', ''),
                    name=item.get('ovrs_item_name', ''),
                    quantity=float(item.get('ovrs_cblc_qty', '0')),
                    avg_price=float(item.get('pchs_avg_pric', '0')),
                    current_price=float(item.get('now_pric', '0')),
                    total_value=float(item.get('ovrs_stck_evlu_amt', '0')),
                    profit_loss=float(item.get('ovrs_evlu_pfls_amt', '0')),
                    profit_loss_rate=float(item.get('evlu_pfls_rt', '0'))
                )
                stocks.append(stock)
        
        account_info.stocks = stocks
        return account_info 