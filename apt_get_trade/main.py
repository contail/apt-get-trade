from fastapi import FastAPI
from apt_get_trade.interfaces.api import api_router

app = FastAPI(
    title="APT-GET-TRADE",
    description="한국투자증권 API를 활용한 트레이딩 애플리케이션",
    version="0.1.0"
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("apt_get_trade.main:app", host="0.0.0.0", port=8000, reload=True) 