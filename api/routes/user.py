import fastapi
from fastapi_sqlalchemy import db
from models import UserInfo
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

router = fastapi.APIRouter(prefix="/user", tags=["user"])

@router.post(path="/login",
    status_code=fastapi.status.HTTP_200_OK,
    description="用户登录",)
def login(username: str, password: str):
    with db():
        result = db.session.query(UserInfo.password).where(UserInfo.user_name==username).scalar()
        if result == password:
            return {"message": "User logged in successfully"}
        else:
            return {"message": "User logged in failed"}


@router.post(path="/add",
    status_code=fastapi.status.HTTP_200_OK,
    description="用户登录",)
def add_user(username: str, password: str):
    with db():
        user=UserInfo(user_name=username,password=password)
        db.session.add(user)
        db.session.commit()

    return {"message": "Add user successfully"}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")