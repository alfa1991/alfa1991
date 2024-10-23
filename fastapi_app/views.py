# fastapi_app/views.py

from fastapi import APIRouter, HTTPException
from typing import List
from models import Item  # Импортируем модель Item

item_router = APIRouter()

# Список товаров (пример данных)
items_db = []

@item_router.get("/items/", response_model=List[Item])  # Получение списка товаров
async def get_items():
    return items_db

@item_router.get("/items/{item_id}", response_model=Item)  # Получение конкретного товара
async def get_item(item_id: int):
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@item_router.post("/items/", response_model=Item)  # Создание нового товара
async def create_item(item: Item):
    items_db.append(item)
    return item

@item_router.put("/items/{item_id}", response_model=Item)  # Обновление товара
async def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@item_router.delete("/items/{item_id}")  # Удаление товара
async def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
