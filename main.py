from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from fastapi.templating import Jinja2Templates
from database.db import Sessionlocal
# from models.orders import Order
from models.products import Product
from parsing import get_goots_from_xlsx


app = FastAPI(title="Мой проект")

templates = Jinja2Templates(directory="templates")


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    context = {
        "request": request,
        "title": "Контакты",
        "adress": "ул. Павловская д.26",
        "phone": "8 (800) 555 35 35",
        "email": "top@secret.com"
    }
    return templates.TemplateResponse("about.html", context=context)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    
    context = {
        "request": request,
        "title": "Контакты",
        "main_text": "Страница для оформления заказа",
        "index": "https://topol-dt.ru/personal"

        
    }
    return templates.TemplateResponse("index.html", context=context)

@app.get("/contacts", response_class=HTMLResponse)
def contacts(request: Request):
    context = {
        "request": request,
        "title": "Контакты",
        "adress": "ул. Павловская д.26",
        "phone": "8 (800) 555 35 35",
        "email": "top@secret.com"
    }
    return templates.TemplateResponse("contacts.html", context=context)




@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    session = Sessionlocal()
    data = session.query(Product).all()
    session.close()
    context = {
        "request": request,
        "title": "Заказы",
        "products": data
    }
    return templates.TemplateResponse("products.html", context=context)



@app.get("/posts", response_class=HTMLResponse)
def posts(request: Request):
    session = Sessionlocal()
    data = session.query(Product).all()
    session.close()
    context = {
        "request": request,
        "title": "Заказы",
        "posts": data
    }
    return templates.TemplateResponse("posts.html", context=context)


@app.get("/products/{id}", response_class=HTMLResponse)
def product_detail(request: Request, id: int):
    session = Sessionlocal()
    product = session.query(Product).filter(Product.id == id).first()
    session.close()
    context = {
        "request": request,
        "title": "Product Detail",
        "product": product
    }
    return templates.TemplateResponse("product_detail.html", context=context)




if __name__ == "__main__":
    get_goots_from_xlsx()
    uvicorn.run("main:app", port=8000, reload=True) 