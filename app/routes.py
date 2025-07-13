
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Geçici veri deposu
urunler = []

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/urunler", response_class=HTMLResponse)
async def list_urunler(request: Request):
    return templates.TemplateResponse("urunler.html", {"request": request, "urunler": urunler})

@router.post("/urun-ekle")
async def urun_ekle(
    ad: str = Form(...),
    numara_araligi: str = Form(...),
    stok: int = Form(...),
    varyant: str = Form(...)
):
    urunler.append({
        "ad": ad,
        "numara_araligi": numara_araligi,
        "stok": stok,
        "varyant": varyant
    })
    return RedirectResponse(url="/urunler", status_code=303)
