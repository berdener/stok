
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
@router.get("/urunler/yeni", response_class=HTMLResponse)
async def yeni_urun_formu(request: Request):
    return templates.TemplateResponse("urunler.html", {"request": request})
import os
import requests

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_API_SECRET = os.getenv("SHOPIFY_API_SECRET")
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")

@router.get("/shopify-urunler", response_class=HTMLResponse)
async def shopify_urunleri_getir(request: Request):
    url = f"https://{SHOPIFY_STORE_URL}/admin/api/2024-04/products.json"
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    return templates.TemplateResponse("shopify_urunler.html", {
        "request": request,
        "urunler": data.get("products", [])
    })
