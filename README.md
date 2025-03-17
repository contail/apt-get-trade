# APT-GET-TRADE
apt-get install apartment을 현실로.
자동매매로 서울숲 트리마제 입성하는 그날까지.

## 📈 About
Python 기반 자동 주식 매매 프로그램입니다. 한국투자증권 OpenAPI를 활용하여 국내 및 해외 주식 실시간 매매를 지원하는 트레이딩 애플리케이션입니다. DDD(Domain-Driven Design) 아키텍처를 적용하여 구현되었습니다.

## 🛠 Features
- 한국투자증권 OpenAPI 연동 (REST / WebSocket)
- 자동 매매 전략 실행
- 종목 모니터링 및 알림
- 거래 로그 저장
- 백테스트 기능 (추가 예정)
- 해외주식 계좌 조회
- 해외주식 잔고 조회

## ⚙️ Tech Stack
- Python 3.x
- FastAPI (백엔드)
- React (프론트, 예정)
- Docker (서버 배포)
- Redis / SQLite (캐시 및 DB)

## 프로젝트 구조
```
apt_get_trade/
├── domain/             # 도메인 계층 (엔티티, 값 객체, 도메인 서비스)
│   └── account/        # 계좌 관련 도메인
├── application/        # 애플리케이션 계층 (유스케이스, 서비스)
│   └── account/        # 계좌 관련 서비스
├── infrastructure/     # 인프라스트럭처 계층 (외부 API, 데이터베이스)
│   ├── external_services/ # 외부 서비스 (한국투자증권 API)
│   └── repositories/   # 리포지토리 구현
├── interfaces/         # 인터페이스 계층 (API, CLI)
│   └── api/           # REST API
└── core/              # 공통 모듈 (설정, 유틸리티)
```

## 설치 및 실행

### 1. 환경 설정
```bash
# 저장소 클론
git clone https://github.com/yourusername/apt-get-trade.git
cd apt-get-trade

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -e .
```

### 2. 환경 변수 설정
`.env.example` 파일을 복사하여 `.env` 파일을 생성하고 필요한 정보를 입력합니다.

```bash
cp .env.example .env
```

### 3. 실행

#### CLI 모드
```bash
python main.py
```

#### API 서버 모드
```bash
python -m apt_get_trade.main
```

## API 엔드포인트
- `GET /account/token` - 접근 토큰 발급
- `GET /account/overseas/balance` - 해외주식 잔고 조회
- `GET /account/overseas/account` - 해외주식 계좌 조회
- `GET /account/overseas/info` - 해외주식 계좌 정보 조회 (도메인 객체)

## 🚀 목표
- 서울숲 트리마제 입성
- 안정적인 자동 매매 수익률 달성

## 📄 License
MIT
