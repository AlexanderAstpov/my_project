from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from fastapi.templating import Jinja2Templates
from database.db import Sessionlocal
# from models.orders import Order
from models.products import Product


app = FastAPI(title="Мой проект")

templates = Jinja2Templates(directory="templates")


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




if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) 