from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Balance:
    """해외주식 잔고 정보"""
    currency: str
    symbol: str
    name: str
    quantity: float
    avg_price: float
    current_price: float
    total_value: float
    profit_loss: float
    profit_loss_rate: float


@dataclass
class AccountInfo:
    """해외주식 계좌 정보"""
    account_number: str
    product_code: str
    currency: str
    cash_balance: float
    total_balance: float
    total_purchase_amount: float
    total_evaluation_amount: float
    total_profit_loss: float
    total_profit_loss_rate: float
    stocks: List[Balance] = None

    @classmethod
    def from_api_response(cls, response_data: dict, account_number: str, product_code: str):
        """API 응답으로부터 계좌 정보 객체 생성"""
        output = response_data.get('output', {})
        
        return cls(
            account_number=account_number,
            product_code=product_code,
            currency=output.get('tr_crcy_cd', 'USD'),
            cash_balance=float(output.get('cash_blnc', '0')),
            total_balance=float(output.get('tot_blnc', '0')),
            total_purchase_amount=float(output.get('pchs_amt_smtl', '0')),
            total_evaluation_amount=float(output.get('evlu_amt_smtl', '0')),
            total_profit_loss=float(output.get('ovrs_tot_pfls', '0')),
            total_profit_loss_rate=float(output.get('ovrs_tot_pfls_rt', '0')),
            stocks=[]
        ) 