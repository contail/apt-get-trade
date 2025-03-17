"""
APT-GET-TRADE 애플리케이션 실행 스크립트
"""
from apt_get_trade.application.account.services import AccountService
import json


def main():
    """메인 함수"""
    try:
        # 계좌 서비스 초기화
        account_service = AccountService()
        
        # 1. 접근 토큰 발급
        access_token = account_service.get_access_token()
        print(f"Access Token 발급 성공: {access_token[:10]}...")
        
        # 2. 해외주식 계좌 정보 조회
        account_info = account_service.get_account_info()
        
        # 3. 결과 출력
        print("\n[해외 계좌 정보]")
        print(f"계좌번호: {account_info.account_number}")
        print(f"통화: {account_info.currency}")
        print(f"현금 잔고: {account_info.cash_balance:,.2f}")
        print(f"총 잔고: {account_info.total_balance:,.2f}")
        print(f"총 매입금액: {account_info.total_purchase_amount:,.2f}")
        print(f"총 평가금액: {account_info.total_evaluation_amount:,.2f}")
        print(f"총 손익: {account_info.total_profit_loss:,.2f}")
        print(f"총 손익률: {account_info.total_profit_loss_rate:.2f}%")
        
        # 4. 보유 주식 정보 출력
        if account_info.stocks:
            print("\n[보유 주식 정보]")
            for stock in account_info.stocks:
                print(f"{stock.symbol} ({stock.name})")
                print(f"  수량: {stock.quantity}")
                print(f"  평균단가: {stock.avg_price:,.2f}")
                print(f"  현재가: {stock.current_price:,.2f}")
                print(f"  평가금액: {stock.total_value:,.2f}")
                print(f"  손익: {stock.profit_loss:,.2f} ({stock.profit_loss_rate:.2f}%)")
                print("---")
        else:
            print("\n보유 주식이 없습니다.")
            
    except Exception as e:
        print(f"오류 발생: {str(e)}")


if __name__ == "__main__":
    main() 