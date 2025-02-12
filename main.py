from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

# FastAPI 애플리케이션 생성
app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:3000",  # React 앱 주소
    "http://127.0.0.1:3000",  # React 앱 주소
]

# CORS 허용 : React에서 API 호출 가능
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 설정된 도메인만
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 메인페이지
@app.get("/")
def a():
    return "hello"

# 서브 페이지
# 서브 페이지를 반환하는 코드에서 경로 오류 확인
@app.get("/sub")
def b():
    return FileResponse('static/index.html') 
# 데이터 받기
class Model(BaseModel):
    name: str
    phone: str

# 데이터 제공 API
@app.get("/api/data")  # 경로 수정: /api/data로 변경
async def get_data():
    # 예시 데이터 반환
    return {"message": "FastAPI connected successfully!"}

# 데이터 받기: POST
@app.post("/send")
def c(data: Model):
    return {"status": "전송완료"}
