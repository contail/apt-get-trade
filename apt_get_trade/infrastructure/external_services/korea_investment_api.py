import requests
import json
from typing import Dict, Any, Optional

from apt_get_trade.core.config import APP_KEY, APP_SECRET, BASE_URL


class KoreaInvestmentAPI:
    """한국투자증권 API 클라이언트"""
    
    def __init__(self):
        self.app_key = APP_KEY
        self.app_secret = APP_SECRET
        self.base_url = BASE_URL
        self.access_token = None
    
    def get_access_token(self) -> str:
        """접근 토큰 발급"""
        url = f"{self.base_url}/oauth2/tokenP"
        headers = {'Content-Type': 'application/json'}
        data = {
            "grant_type": "client_credentials",
            "appkey": self.app_key,
            "appsecret": self.app_secret
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            return self.access_token
        else:
            raise Exception(f"Access Token 발급 실패: {response.text}")
    
    def get_overseas_balance(self, account_no: str, product_code: str, exchange_code: str = 'NASD', currency: str = 'USD') -> Dict[str, Any]:
        """해외주식 잔고 조회"""
        if not self.access_token:
            self.get_access_token()
            
        url = f"{self.base_url}/uapi/overseas-stock/v1/trading/inquire-balance"
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'authorization': f'Bearer {self.access_token}',
            'appkey': self.app_key,
            'appsecret': self.app_secret,
            'tr_id': 'TTTS3012R',  # 실전 투자용 거래 ID
            'custtype': 'P'        # 개인 고객
        }
        params = {
            'CANO': account_no,
            'ACNT_PRDT_CD': product_code,
            'OVRS_EXCG_CD': exchange_code,
            'TR_CRCY_CD': currency,
            'CTX_AREA_FK200': '',
            'CTX_AREA_NK200': ''
        }
        
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"잔고 조회 실패: {response.text}")
    
    def get_overseas_account(self, account_no: str, product_code: str, exchange_code: str = 'NASD') -> Dict[str, Any]:
        """해외주식 계좌 조회"""
        if not self.access_token:
            self.get_access_token()
            
        url = f"{self.base_url}/uapi/overseas-stock/v1/trading/inquire-present-balance"
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'authorization': f'Bearer {self.access_token}',
            'appkey': self.app_key,
            'appsecret': self.app_secret,
            'tr_id': 'TTTS3012R',  # 실전 투자용 거래 ID
            'custtype': 'P'        # 개인 고객
        }
        params = {
            'CANO': account_no,
            'ACNT_PRDT_CD': product_code,
            'OVRS_EXCG_CD': exchange_code,
            'WCRC_FRCR_DVSN_CD': 'D',  # 원화/외화 구분 (D: 원화)
            'NATN_CD': '840',          # 국가코드 (미국: 840)
            'TR_MKET_CD': '00',        # 거래시장코드 (전체)
            'INQR_DVSN_CD': '00'       # 조회구분코드 (00: 전체)
        }
        
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"계좌 조회 실패: {response.text}") 