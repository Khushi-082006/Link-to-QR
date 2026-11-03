from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path
import qrcode
BASE_DIR= Path(__file__).resolve().parent
QR_FOLDER = BASE_DIR / "static" / "qrcodes"
QR_FOLDER.mkdir(parents=True,exist_ok=True)

app=FastAPI()
template= Jinja2Templates(directory= str(BASE_DIR/"template"))

app.mount("/static",StaticFiles(directory=str(BASE_DIR/"static")),
          name="static"
          )
class QRRequest(BaseModel):
    link:str

@app.get("/",response_class=HTMLResponse)
def home(request: Request):
    return template.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

@app.post("/qr")
def generate_qr(data:QRRequest):
    link=data.link.strip()
    if not link :
        return {"error":"Please enter a link"}
    qr=qrcode.make(link)
    qr.save(QR_FOLDER/"myqr.png")
    return {"imageUrl":"/static/qrcodes/myqr.png"}
