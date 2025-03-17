import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# API 인증 정보
APP_KEY = os.getenv('APP_KEY', '발급받은_APP_KEY')
APP_SECRET = os.getenv('APP_SECRET', '발급받은_APP_SECRET')
ACCOUNT_NO = os.getenv('ACCOUNT_NO', '810XXXXX')  # 종합계좌번호 앞 8자리
PRODUCT_CODE = os.getenv('PRODUCT_CODE', '01')    # 계좌상품코드 뒤 2자리
BASE_URL = os.getenv('BASE_URL', 'https://openapi.koreainvestment.com:9443') 