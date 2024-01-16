from fastapi import FastAPI, WebSocket
from api import router 
from configs import settings
from fastapi_sqlalchemy import DBSessionMiddleware
from models.db.session import engine, session_args
from fastapi.responses import HTMLResponse
PREFIX = f"/{settings.PROJECT_NAME}"

app = FastAPI(itle="pydocker service",
        description="pydocker后台服务",
        contact={"email": "wq@bielcrystal.com"},
        openapi_url=f"{PREFIX}/openapi.json",
        docs_url=f"{PREFIX}/docs",)

app.include_router(router=router, prefix=PREFIX)
app.add_middleware(
        DBSessionMiddleware, custom_engine=engine, session_args=session_args
    )

#@app.websocket("/ws")
#async def websocket_endpoint(websocket: WebSocket):
#    await websocket.accept()
#    while True:
#        data = await websocket.receive_text()
#        await websocket.send_text(f"Message text was: {data}")
        

        
